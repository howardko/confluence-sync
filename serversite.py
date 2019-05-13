import functools
import time
import urllib

import requests
import requests.exceptions
from requests.auth import HTTPBasicAuth


def add_content(site_url, username, password, data):
    url = "{}/rest/api/content".format(site_url)
    resp = requests.post(url,
        auth=HTTPBasicAuth(username, password),
        json=data)
    resp.raise_for_status()
    return resp.json()


def add_attachment(site_url, username, password, page_id, filename):
    url = "{}/rest/api/content/{}/child/attachment".format(site_url, page_id)
    headers = {"X-Atlassian-Token": 'nocheck'}
    files = {'file': open(filename,'rb')}
    values = {'minorEdit': 'true'}

    # check if file name contains unicode
    filename_has_unicode = False
    try:
        filename = filename.encode('ascii')
    except UnicodeEncodeError:
        files = {'file': (urllib.quote(filename.encode('utf-8')), open(filename, 'rb').read())}
        filename_has_unicode = True

    # upload file
    func_to_call = functools.partial(requests.post, url,
        auth=HTTPBasicAuth(username, password),
        headers=headers, files=files, data=values)
    while True:
        try:
            print('upload ' + filename)
            resp = func_to_call()
            resp.raise_for_status()
            break
        except requests.exceptions.HTTPError as e:
            print(resp.text)
            if e.response.status_code == 500:
                time.sleep(1)
                continue
            else:
                raise

    print(resp.json())
    attachment_id = resp.json()['results'][0]['id']
    

    # change filename back
    if filename_has_unicode:
        url = "{}/rest/api/content/{}/child/attachment/{}".format(site_url, page_id, attachment_id)
        data = {
            "version": {
                "number": 1
            },
            "id": attachment_id,
            "type": "attachment",
            "title": filename
        }
        resp = requests.put(url,
            auth=HTTPBasicAuth(username, password),
            json=data)
        resp.raise_for_status()
        return resp.json()
