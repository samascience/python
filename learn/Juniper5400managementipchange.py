import paramiko
import time
import socket
import sys

Spineip = "10.255.0.1"
Leafip = "10.201.0."
NewLeafIP = "10.137.1."
x=11
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("Spineip",username="root",password="Apples!234")
ssh_shell=ssh.invoke_shell()
ssh_shell.send("cli \n")
while (x < 5):
    Intoleafip = Leafip+str(x)
    NewLeafIP1 = NewLeafIP+str(x)
    print(Intoleafip)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("Intoleafip",username="root",password="Apples!234")
    ssh_shell=ssh.invoke_shell()
    ssh_shell.send("cli \n")
    print "For iteration : " + str(x)
    ssh_shell.send("show version\n")
    # ssh_shell.send("edit \n" )
    # ssh_shell.send("set system ntp server 216.239.35.0 prefer \n")
    # ssh_shell.send("set routing-options static route 0.0.0.0/0 next-hop 10.137.0.1 \n")
    # ssh_shell.send("delete interfaces em0 \n")
    # ssh_shell.send("set interfaces em0 unit 0 family inet address "+NewLeafIP+"\n")
    # ssh_shell.send("show | compare \n")
    # ssh_shell.send("commit \n")
    x = x+1
    time.sleep(5)
    output=ssh_shell.recv(9600)
    print "output" + output
    ssh_shell.send("exit \n")
