import os,csv,argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d',help='pass the csv file',default='Error: .csv must be specified')
args = parser.parse_args()
file1 = open(args.d,'rb')
reader = csv.reader(file1)
for row in reader:
    for i in [5,6,7,8]:
        str1 = "curl -s -u admin:1234 http://"+row[0]+"/outlet?"+str(i)+"=OFF"
        curlOut = os.system(str1)
        if curlOut != 0:
            print "Failed to execute curl cmd"
        else:
            print "Successfully executed curl cmd"
            print "check for voltage value"
            raw_input("enter any command to continue: ")
            str2 = "curl -s -u admin:1234 http://"+row[0]+"/outlet?"+str(i)+"=ON"
            curlOut1 = os.system(str2)
            if curlOut1 != 0:
                print "Failed to execute curl cmd"
            else:
                print "Successfully executed curl cmd"
