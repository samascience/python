import paramiko
import time
import socket
import sys
import os

ip="10.137.10."
x=2
while(True):
    tip = ip+str(x)   
    rep = os.system('ping -c 3 ' +tip)
    if rep == 0:
        print "switch is up"  +tip
    else:
		print "switch is down"  +tip
    x = x+1 
	
			