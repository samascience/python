import paramiko
import time
import socket 
import sys 
ip="10.255.7."
x=2

raw = raw_input('press y to continue')

if raw == 'y':
    tip = ip+str(x) 
    print(tip)
