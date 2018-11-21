import sys,telnetlib,os,csv,re,argparse
parser = argparse.ArgumentParser()
#parser.add_argument('-d','-fans',help='pass the csv file',default='Error: .csv must be specified')
parser.add_argument('-d',help='pass the csv file',default='Error: .csv must be specified')
parser.add_argument('-fans',help='pass the csv  fans file',default='Error: fans .csv must be specified')
args = parser.parse_args()
#parser.parse_args(['-h'])
file1 = open(args.d,'rb')
reader = csv.reader(file1)
for row in reader:
    tn = telnetlib.Telnet(row[0],row[1])
    tn.write("set cli screen-length 0\r\n")
    tn.read_until(">",5)
    tn.write("show chassis hardware\r\n")
    out = tn.read_until(">")
    out = out.split("AFI")
    fan_file = open(args.fans,'rb')
    fan_reader = csv.reader(fan_file)
    fan_list = list(fan_reader)
    for i in range(0,len(fan_list)):
        out[i+2] = ",".join(out[i+2])
        str1 = str(fan_list[i][0]+'\W+'+fan_list[i][1]+'\W+'+fan_list[i][2])
        if (re.match(out[i+2],str1)!= None):
                print "value mismatched"
        else:
                print "value matched"
    tn.write("logout\r\n")
    tn.close
