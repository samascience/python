import requests
from requests.auth import HTTPDigestAuth
import os,csv,argparse
import pandas as pd
parser = pd.DataFrame()
data= pd.read_excel('IP.xlsx', sheet_name="Sheet2")
df=pd.DataFrame(data)
i = 0
headers = {
    'X-Requested-With': "XMLHttpRequest",
    }
for index,row in df.iterrows():
    r1 = row.values
    url = "https://"+r1[0]+"/restapi/config/allow_plaintext_logins/"
    payload = "true"
    #response = requests.request("PUT", url, data=payload, headers=headers, auth=HTTPDigestAuth('admin','1234'), verify=False)
    print ( url )
    #print(response.text)
