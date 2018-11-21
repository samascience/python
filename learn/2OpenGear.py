import paramiko
import time
import socket
import sys
import os

ip="10.137.11."
True=1
x=20
ipad= "192.168.0.1"
tip1 = str(ipad)
while(True):
    tip = ip+str(x)   #10.137.11.3
    rep = os.system('ping -c 3 ' +ipad)
    if rep == 0:
        print "switch is up"
        rep1 = raw_input("press y to move to next switch : " )
        if rep1 == 'y':
            time.sleep(10)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("192.168.0.1", username="root", password="default")
            ssh_shell = ssh.invoke_shell()
            ssh_shell.send("config -s config.interfaces.wan.mode=static \n" )
            ssh_shell.send("config -s config.interfaces.wan.address="+tip+"\n" )
            ssh_shell.send("config -s config.interfaces.wan.netmask=255.255.0.0 \n" )
            ssh_shell.send("config -s config.interfaces.wan.dns1=10.137.10.1  \n" )
            ssh_shell.send("config -s config.interfaces.wan.gateway=10.137.10.1  \n")
            ssh_shell.send("config -r ipconfig \n" )
            x=x+1
            time.sleep(2)
            output = ssh_shell.recv(9600)
            print( "output" + output)
    else:
        print("The device is not reachable with ip address "+ ipad)
