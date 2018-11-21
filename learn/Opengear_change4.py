import paramiko
import time
import socket
import sys
import os

ip="10.137.11."
True=1
x=2

while(True):
    tip = ip+str(x)   #10.137.11.3
    time.sleep(5)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect( tip, username="root", password="default")
    ssh_shell = ssh.invoke_shell()
    ssh_shell.send("config -s config.interfaces.wan.mode=static \n" )
    ssh_shell.send("config -s config.interfaces.wan.netmask=255.255.248.0 \n" )
    ssh_shell.send("config -s config.interfaces.wan.gateway=10.137.8.1  \n")
    ssh_shell.send("config -r ipconfig \n" )
    x=x+1
    time.sleep(2)
    output = ssh_shell.recv(9600)
    print( "output" + output)
    
