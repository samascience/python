import paramiko
import time
import socket
import sys
import os

ip="10.137.11."

x=2

while(x < 4):
    tip = ip+str(x)   #10.137.11.3
    rep = os.system('ping -c 3 ' +tip)
    if rep == 0:
        print "switch is up"
        rep1 = raw_input("press y to move to next switch : " )
        if rep1 == 'y':
            time.sleep(10)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(tip, username="root", password="default")
            ssh_shell = ssh.invoke_shell()
            ssh_shell.send("setfset | grep 'Serial number' \n" )
            x=x+1
            time.sleep(2)
            output = ssh_shell.recv(9600)
            print( "output" + output)
    else:
        print("The device is not reachable with ip address "+ ipad)
