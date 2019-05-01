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
    return resp.json()
