import paramiko
import time
import socket
import sys

print "Start"
Spineip = "10.255.0.1"
Leafip = "10.201.0."
NewLeafIP = "10.137.1."
x=11
try:
    print "into try block"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(Spineip,username="root",password="Apples!234")
    ssh_shell=ssh.invoke_shell()
    ssh_shell.send("cli \n")

    while (x < 16):
        try:
            Intoleafip = Leafip+str(x)
            NewLeafIP1 = NewLeafIP+str(x)
            print(Intoleafip)

            trasnport = ssh_shell.get_transport()
            leaf_addr = (Intoleafip, 22)
            spine_addr = (Spineip, 22)

            leaf_conn = trasnport.open_channel("direct-tcpip", leaf_addr, spine_addr)

            leaf_ssh = paramiko.SSHClient()
            leaf_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            leaf_ssh.connect(Intoleafip,username="root",password="Apples!234", sock=leaf_conn)
            leaf_ssh_shell=leaf_ssh.invoke_shell()
            print "into SSh of leaf"
            leaf_ssh_shell.send("cli \n")
            time.sleep(2)
            leaf_ssh_shell.recv(9000)

            print "For iteration : " + str(x)
            leaf_ssh_shell.send("show version\n")
            time.sleep(5)
            leaf_ssh_shell.recv(15000)

            leaf_ssh.close()
            x = x +1

            # ssh_shell.send("ssh root@"+Intoleafip+"\n")
            # ssh_shell.send("Apples!234\n")
            # #ssh_shell.send("yes\n")
            # ssh_shell.send("cli\n")
            # ssh_shell.send("show version\n")

            # vmtransport = vm.get_transport()
            # dest_addr = ('10.103.53.26', 22) #edited#
            # local_addr = ('192.168.115.103', 22) #edited#
            # vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)
            # #
            # jhost=paramiko.SSHClient()
            # jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # #jhost.load_host_keys('/home/osmanl/.ssh/known_hosts') #disabled#
            # jhost.connect('10.103.53.26', username='latiu', password='xxxx', sock=vmchannel)

            # ssh = paramiko.SSHClient()
            # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh.connect(Intoleafip,username="root",password="Apples!234")
            # ssh_shell=ssh.invoke_shell()
            # ssh_shell.send("cli \n")
            # print "For iteration : " + str(x)
            # ssh_shell.send("show version\n")
            # ssh_shell.send("edit \n" )
            # ssh_shell.send("set system ntp server 216.239.35.0 prefer \n")
            # ssh_shell.send("set routing-options static route 0.0.0.0/0 next-hop 10.137.0.1 \n")
            # ssh_shell.send("delete interfaces em0 \n")
            # ssh_shell.send("set interfaces em0 unit 0 family inet address "+NewLeafIP+"\n")
            # ssh_shell.send("show | compare \n")
            # ssh_shell.send("commit \n")
            # x = x+1
            # time.sleep(5)
            # output=ssh_shell.recv(9600)
            # print "output" + output
            # ssh_shell.send("exit \n")
        except paramiko.SSHException :
            print "{} is not reachable \n".format(Intoleafip)
            #print Intoleafip + " is not reachable \n"
            continue
    ssh.close()
except paramiko.SSHException:
    print "Error in SSH "
