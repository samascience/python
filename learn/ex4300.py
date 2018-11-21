import paramiko
import time
import socket
import sys

LeafMGMTip = "10.137.0."

x = 25
while (x < 44) :
	Intoleafip = LeafMGMTip+str(x)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(Intoleafip,username="root",password="Apples!234")
	ssh_shell=ssh.invoke_shell()
	ssh_shell.send("cli \n")
	ssh_shell.send("edit \n" )
	ssh_shell.send("set interfaces ge-0/0/0 unit 0 family ethernet-switching interface-mode access vlan members VLAN_4000   \n")
	ssh_shell.send("show | compare \n")
	ssh_shell.send("commit \n")
	x = x+1
	time.sleep(5)
	output=ssh_shell.recv(9600)
	print "output" + output
	ssh_shell.send("exit \n")
	ssh.close()
    