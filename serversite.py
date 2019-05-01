import requests
from requests.auth import HTTPBasicAuth

def add_content(site_url, username, password, data):
    url = "{}/rest/api/content".format(site_url)
    resp = requests.post(url,
        auth=HTTPBasicAuth(username, password),
        json=data)
    return resp.text