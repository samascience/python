import os,csv,argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d',help='pass the csv file',default='Error: .csv must be specified')
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
