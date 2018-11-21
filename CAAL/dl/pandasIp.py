import os,csv,argparse
import pandas as pd
parser = pd.DataFrame()
data= pd.read_excel('IP.xlsx', sheet_name="Sheet2")
df=pd.DataFrame(data)
i = 0
for index,row in df.iterrows():
    r1 = row.values
    #r2 = r1.str()
    #print r1[0]
    #print("Printed the value")
    str1 = "curl -u admin:1234 http://"+r1[0]+"/network.cgi?ipaddr="+r1[0]+"&netmask=255.255.248.0&gateway=10.137.8.1 \n"
	#str1 = "curl  -X PATCH -H "Content-Type: application/json-patch+json"  --data [{\"op\":\"replace\",\"path\":\"\/gateway\",\"value\":\""+r1[0]+"\"},{\"op\":\"replace\",\"path\":\"\/netmask\",\"value\":\"255.255.248.0\"},{\"op\":\"replace\",\"path\":\"\/ip_address\",\"value\":\"10.137.8.1\"}] --digest "http://admin:1234@"+r1[0]+"/restapi/network/wired/""
    #str2 = "curl -u admin:1234 -X PUT -H "X-CSRF: x" --data "value=false" --digest http://"+r1[0]+"/restapi/network/same_subnet_only/"
    #str3 = " \n "
    print  str1
    '''curlOut = os.system(str1)
    #curlOut = os.system(str2)
    curlOut = os.system(str3)
    if curlOut != 0:
        print "Failed to execute curl cmd "+ r1
    else:
        print "Successfully executed curl cmd "+ r1
		
		'''


'''
h = data.columns.tolist()


args = parser.parse_args()
file1 = open(args.d,'rb')
reader = csv.reader(file1)
for row in reader:
    for i in [5,6,7,8]:
        str1 = "curl -u admin:1234 http://"+row[0]+"/network.cgi?ipaddr="+row[0]+"&netmask=255.255.248.0&gateway=10.137.8.1"
        curlOut = os.system(str1)
        if curlOut != 0:
            print "Failed to execute curl cmd "+  row[0]
        else:
            print "Successfully executed curl cmd "+ row[0]
            
'''