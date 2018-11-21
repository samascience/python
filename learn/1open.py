import paramiko
import time
import socket
import sys
import os

ip="10.255.7."
ip1="10.137.11."
True=1
x=2

while True:
	tip = ip+str(x)
	tip1=ip1+str(x)
	print "Changing Ip from "+tip+" to "+tip1
	rep=os.system("ping -c 1  "+ tip)
	if rep == 0:
		print "switch is up"
		time.sleep(2)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(str(tip), username="root", password="default")
		ssh_shell = ssh.invoke_shell()
		ssh_shell.send("config -s config.interfaces.wan.mode=static \n" )
		ssh_shell.send("config -s config.interfaces.wan.address="+tip1+"\n" )
		ssh_shell.send("config -s config.interfaces.wan.netmask=255.255.254.0 \n" )
		ssh_shell.send("config -s config.interfaces.wan.dns1=10.137.10.1  \n" )
		ssh_shell.send("config -r ipconfig \n" )
		time.sleep(5)
		output = ssh_shell.recv(9600)
		print "output" + output
		x=x+1
	else:
		print "server "+tip+" is down"
		time.sleep(10)
