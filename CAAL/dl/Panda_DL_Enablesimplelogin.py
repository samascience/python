import os,csv,argparse
import pandas as pd
import requests
from requests.auth import HTTPDigestAuth
parser = pd.DataFrame()
data= pd.read_excel('IP.xlsx', sheet_name="Sheet5")
df=pd.DataFrame(data)
i = 0
headers = {
    'X-Requested-With': "XMLHttpRequest",
    }
payload1 = "true"
payload2 = "255.255.248.0"
payload3 = "10.137.8.1"
payload4 = "false"
for index,row in df.iterrows():
    r1 = row.values
    #r2 = r1.str()
    #print r1[0]
    #print("Printed the value")
    #str1 = url = "https://"+r1[0]+"/restapi/config/allow_plaintext_logins/"
    #response1 = requests.request("PUT", str1, data=payload1, headers=headers, auth=HTTPDigestAuth('admin','1234'), verify=False)
    #str2 = "https://"+r1[0]+"/restapi/network/wired/netmask/"
    #response2 = requests.request("PUT", str2, data=payload2, headers=headers, auth=HTTPDigestAuth('admin','1234'), verify=False)
    #str3 ="https://"+r1[0]+"/restapi/network/wired/gateway/"
    #response3 = requests.request("PUT", str3, data=payload3, headers=headers, auth=HTTPDigestAuth('admin','1234'), verify=False)
    str4 = "https://"+r1[0]+"/restapi/network/same_subnet_only/"
    response4 = requests.request("PUT", str4, data=payload4, headers=headers, auth=HTTPDigestAuth('admin','1234'), verify=False)
	#str1 = "curl  -X PATCH -H "Content-Type: application/json-patch+json"  --data [{\"op\":\"replace\",\"path\":\"\/gateway\",\"value\":\""+r1[0]+"\"},{\"op\":\"replace\",\"path\":\"\/netmask\",\"value\":\"255.255.248.0\"},{\"op\":\"replace\",\"path\":\"\/ip_address\",\"value\":\"10.137.8.1\"}] --digest "http://admin:1234@"+r1[0]+"/restapi/network/wired/""
    #str2 = "curl -u admin:1234 -X PUT -H "X-CSRF: x" --data "value=false" --digest http://"+r1[0]+"/restapi/network/same_subnet_only/"
    #str3 = " \n "
    #print  str1
    #print  str2
    #print  str3
    print  str4
    #print  response1
    #print  response2
    #print  response3
    print  response4
