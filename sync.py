# -*- coding: utf-8 -*-
import os

import begin
from bs4 import BeautifulSoup, CData

import cloudsite
import serversite


def _sync_content(
        cloud_site_url, cloud_site_username,
        cloud_site_api_token, cloud_site_page_id,
        server_site_url, server_site_username,
        server_site_password, server_site_space_key,
        server_site_ancestor_id):
    # get cloud page
    resp = cloudsite.get_content(cloud_site_url, cloud_site_username, cloud_site_api_token, cloud_site_page_id)

    # process storage value
    storage_value = resp['body']['storage']['value']

    # parse storage value
    soup = BeautifulSoup(storage_value, features="html.parser")
    for macro in soup.find_all('ac:structured-macro'):
        # only process plantumlcloud
        if macro.get('ac:name') != 'plantumlcloud':
            continue

        # get data
        cloud_data = ''
        for macro_parameter in macro.find_all('ac:parameter'):
            if macro_parameter.get('ac:name') != 'data':
                continue
            cloud_data = macro_parameter.contents
            if cloud_data:
                cloud_data = cloud_data[0]
        if not cloud_data:
            continue

        # decompress data
        converted_cloud_data = cloudsite.decompress_plantuml_data(cloud_data)

        # modify content
        if macro.get('ac:name') == 'plantumlcloud':
            macro['ac:name'] = 'plantuml'
            new_text_body_tag = soup.new_tag("ac:plain-text-body")
            new_text_body_tag.append(CData(converted_cloud_data))
            macro.append(new_text_body_tag)
    converted_storage_value = soup.encode()

    # convert data
    data_to_create = {
        "title": resp['title'],
        "type": resp['type'],
        "space": {
            "key": server_site_space_key
        },
        "ancestors": [
            {
                "id": server_site_ancestor_id
            }
        ],
        "body": {
            "storage": {
                "value": converted_storage_value,
                "representation": resp['body']['storage']['representation']
            }
        }
    }

    # add content
    resp = serversite.add_content(
        server_site_url, server_site_username,
        server_site_password, data_to_create)
    print(resp)
    return resp['id']


def _sync_attachment(
        cloud_site_url, cloud_site_username, cloud_site_api_token,
        cloud_site_cookie, cloud_site_page_id,
        server_site_url, server_site_username,
        server_site_password, page_id):
    # get cloud page attachment list
    resp = cloudsite.get_attachment(cloud_site_url, cloud_site_username, cloud_site_api_token, cloud_site_page_id)
    attachments = resp['results']

    # loop to process attachments
    for attachment in attachments:
        filename = attachment['title']
        print('process attachment ' + filename)
        cloudsite.download_attachment(cloud_site_url, cloud_site_cookie, attachment)
        resp = serversite.add_attachment(server_site_url, server_site_username,
            server_site_password, page_id, filename)
        os.remove(filename)
        print(resp)


@begin.start
def run(cloud_site_url='https://xxx.atlassian.net/wiki',
    cloud_site_username='xxx@xxx.com',
    cloud_site_api_token='5IZlhpPLCBfdfNfjWyXXXXXX',
    cloud_site_cookie='',
    cloud_site_page_id=141000000,
    server_site_url='https://xxxx.qnap.com.tw',
    server_site_username='xxx',
    server_site_password='xxxxxxxx',
    server_site_space_key='QCLOUD',
    server_site_ancestor_id=14870000):

    # sync content
    page_id = _sync_content(
        cloud_site_url, cloud_site_username,
        cloud_site_api_token, cloud_site_page_id,
        server_site_url, server_site_username,
        server_site_password, server_site_space_key,
        server_site_ancestor_id)

    # sync attachment
    _sync_attachment(
        cloud_site_url, cloud_site_username, cloud_site_api_token,
        cloud_site_cookie, cloud_site_page_id,
        server_site_url, server_site_username,
        server_site_password, page_id)
