import sys,telnetlib,os,csv,re,argparse
parser = argparse.ArgumentParser()
#parser.add_argument('-d',action='store',dest='d',type=str,help='pass the csv file',default='Error: .csv must be specified')
parser.add_argument('-d',help='pass the csv file',default='Error: .csv must be specified')
args = parser.parse_args()
#parser.parse_args(['-h'])
file1 = open(args.d,'rb')
reader = csv.reader(file1)
for row in reader:
    tn = telnetlib.Telnet(row[0], row[1])
    tn.read_until(b"login :", 2)
    tn.write(b"root\n")
    tn.read_until(b"Password :", 2)
    tn.write(b"root\n")
    tn.write("\r")
    b = tn.read_until(b"=>", 2)
    if re.findall('CLX3001', b):
        print "string matched.login success"
        #Place holder for get hostname from CAAL
    else:
        print "string did not matched.login failed"
