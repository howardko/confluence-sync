import base64
import zlib
import urllib

import requests
from requests.auth import HTTPBasicAuth

def decompress_plantuml_data(in_data):
    in_data_b64decoded = base64.b64decode(in_data)
    out_data = zlib.decompress(in_data_b64decoded, -15)
    out_data = urllib.unquote(out_data)
    return out_data


def get_content(site_url, username, api_token, page_id):
    url = "{}/rest/api/content/{}?expand=body.storage".format(
        site_url, page_id)
    resp = requests.get(url,
        auth=HTTPBasicAuth(username, api_token))
    resp.raise_for_status()
    return resp.json()


def get_attachment(site_url, username, api_token, page_id):
    url = "{}/rest/api/content/{}/child/attachment?limit=1000".format(
        site_url, page_id)

    # get attachment
    resp = requests.get(url,
        auth=HTTPBasicAuth(username, api_token))
    resp.raise_for_status()
    return resp.json()


def download_attachment(site_url, cookie, attachment):
    filename = attachment['title']
    headers = {"cookie": cookie}
    url = "{}/{}".format(site_url, attachment['_links']['download'])
    resp = requests.get(url, headers=headers, allow_redirects=True)
    resp.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return filename
    