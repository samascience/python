import requests
from requests.auth import HTTPDigestAuth
url = "http://10.137.10.8/restapi/network/wired/gateway/"

payload = "10.137.11.1"
headers = {
    'X-Requested-With': "XMLHttpRequest",
    }

response = requests.request("PUT", url, data=payload, headers=headers, auth=HTTPDigestAuth('admin','1234'))

print(response.text)
