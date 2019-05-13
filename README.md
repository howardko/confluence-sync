# confluence-sync
sync confluence from cloud to server site

# Cloud Site

## Authentication
Basic Authentication with User Name and API Token (applied on https://confluence.atlassian.com/cloud/api-tokens-938839638.html)

## API Doc
https://developer.atlassian.com/cloud/confluence/rest/

## PlantUML
The data is base64_encode(zlib_compress(url_encode(plaintext_data))). There's no header in the zlib data, so you need to manually set wbits to -15 at decompress.
```
<ac:structured-macro ac:name="plantumlcloud" ac:schema-version="1" ac:macro-id="b32c3b08-4e2e-4c8c-a1b9-ccd34ff8d786">
<ac:parameter ac:name="autoSize">true</ac:parameter>
<ac:parameter ac:name="filename">test_flow.png</ac:parameter>
<ac:parameter ac:name="data">vVRtb9owEP41SNuHIMfh9SOhRe2nsRWkfYuO2AGPYKex05X++p3tAKELLVW1SZEd23fPvTx3V0BpRCoKkKZDSYfSpeYlbngAjcuyQybFa5nvOyGe8TeGdMsla4jHbeJzvJAWFd8Ku87vGypzVMFvGXSi27gTTfBqWnIwHH8q5wxx5sgktiJLLx43xTc83eLOn3i5xz0kTkdWhlsDvzfcbByO3SyssNemFOu1v1a4FCrPcctU6ZGk0Qczc29m/u1hYQMaxlAI61yZd4Y3HTp7FBmuTyEuNSjizyT/nWQi54mQCSSZyhkaIxOpXGQ5z2x2VFZn4AF2RW4ffvDHimtjTWKiapNow6f8OiuU3C0Wc3wNuyGi3CmPRwkrVbFSz12H1sXkPomUdzGcbqp2KDmpzEaV4gWMUNKrxBxKB4lx41cj1NwkkKZc68QorAObDPwQBS+L2iIURS5Sj0dnvzRuB4FguoFS81qwMlkwOr3dylQxIdf+cf0isHCmNgKe5bY2yORnUKcquL/xUt7DEiRTu6SqBDt6FCu29xm1MsQJnz5a5zMRDGkXZm+r0yNSOqY9OmYjCr2QjyPSG7nSnV4GwXxYFMh1DdNi8UzRk5YUYDZNwyfSW+2dQ9gKMPuCNwHAFjR9rWgrtsV7ZyrRqirTBsh7rgvWNEivcdV2TUNnY0yh3Wl2CNjVIp3t9vZgO3hWYK0rCag4o9eHVNWT7LpQjNjxFyXPMjiHVGQixcMCX3H7snxwLwM7dUACg6/t/thCs6ubjsT1PHazn1nHGYAFszkOgfh8COhCSW2V3K9Gv1z53nFgtvHdYaqkwVILFo74tlaLYrxPD212c+ixS+1AGRg4JaD/V8ouJpGKHax50kLukVv+7KKr2XXyltuQXuqoAzGw1k3QFcit3vtpsCqV2uZ7+TYC5s9wloA5K1YSRkEYBqS3IGO8pREuhARk6PYWWg9wO95M0sdaJOytxkGYMRpAChD0Wda/pmlscWqD+TtihdEo6o+HdDBs1/Q1+G6X/BNC3w7pTULlPv0kl9F/4zLLVnQYwCDiQTjiBBdgnyFzEPX7HyDzeNNvGzd/AA==</ac:parameter>
<ac:parameter ac:name="width">800</ac:parameter>
<ac:parameter ac:name="compressed">true</ac:parameter>
<ac:parameter ac:name="height">600</ac:parameter>
</ac:structured-macro>
```

# Server Site

## Authentication
Basic Authentication with User Name and Password

## API Doc
https://developer.atlassian.com/server/confluence/confluence-server-rest-api/


## PlantUML
The data is plaintext
```
<ac:structured-macro ac:name="plantuml" ac:schema-version="1" ac:macro-id="9099081f-f7c7-456e-8e37-1d28068ebb8d">
<ac:parameter ac:name="format">PNG</ac:parameter>
<ac:parameter ac:name="title">Test Flow</ac:parameter>
<ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter>
<ac:plain-text-body><![CDATA[@startuml\nactor User\n@enduml\n\n]]></ac:plain-text-body>
</ac:structured-macro>
```

# Usage
```
usage: sync.py [-h] [--cloud-site-url CLOUD_SITE_URL]
               [--cloud-site-username CLOUD_SITE_USERNAME]
               [--cloud-site-api-token CLOUD_SITE_API_TOKEN]
               [--cloud-site-page-id CLOUD_SITE_PAGE_ID]
               [--server-site-url SERVER_SITE_URL]
               [--server-site-username SERVER_SITE_USERNAME]
               [--server-site-password SERVER_SITE_PASSWORD]
               [--server-site-space-key SERVER_SITE_SPACE_KEY]
               [--server-site-ancestor-id SERVER_SITE_ANCESTOR_ID]

optional arguments:
  -h, --help            show this help message and exit
  --cloud-site-url CLOUD_SITE_URL
                        (default: https://xxx.atlassian.net/wiki)
  --cloud-site-username CLOUD_SITE_USERNAME
                        (default: xxx@xxx.com)
  --cloud-site-api-token CLOUD_SITE_API_TOKEN
                        (default: 5IZlhpPLCBfdfNfjWyXXXXXX)
  --cloud-site-page-id CLOUD_SITE_PAGE_ID, -c CLOUD_SITE_PAGE_ID
                        (default: 141000000)
  --server-site-url SERVER_SITE_URL
                        (default: https://xxxx.qnap.com.tw)
  --server-site-username SERVER_SITE_USERNAME
                        (default: xxx)
  --server-site-password SERVER_SITE_PASSWORD
                        (default: xxxxxxxx)
  --server-site-space-key SERVER_SITE_SPACE_KEY
                        (default: QCLOUD)
  --server-site-ancestor-id SERVER_SITE_ANCESTOR_ID, -s SERVER_SITE_ANCESTOR_ID
                        (default: 14870000)
```
