import paramiko,os,csv,re,argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d',help='pass the csv file',default='Error: .csv must be specified')
args = parser.parse_args()
file1 = open(args.d,'rb')
reader = csv.reader(file1)
for row in reader:
    ip=str(row[0])
    port=22
    username='root'
    password='root'
    cmd='uname -a'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    print outlines
    resp=''.join(outlines)
    if re.findall('CLX3001', resp):
        print "string matched.login success"
    else:
        print "string did not matched.login failed"
    ssh.close()
