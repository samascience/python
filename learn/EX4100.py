import paramiko
import time
import socket 
import sys 

ip="10.255.10."
True=1 
x=11
while True:
    tip = ip+str(x) 
    print(tip)
    rep=os.system('ping' + tip)
    if rep == 0:
        print("switch is up")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("tip", username="root", password="Apples!234")
        ssh_shell = ssh.invoke_shell()
        ssh_shell.send("cli \n" )
        ssh_shell.send("edit \n" )
        ssh_shell.send("set interfaces interface-range MGMT_PORT member-range ge-0/0/0 to ge-0/0/47 \n" )
        ssh_shell.send("set interfaces interface-range MGMT_PORT unit 0 family ethernet-switching interface-mode access \n" )
        ssh_shell.send("set interfaces interface-range MGMT_PORT unit 0 family ethernet-switching vlan members VLAN_4000 \n" )
        ssh_shell.send("Show | compare \n")
        output = ssh_shell.recv(9600)
        print("output" + output)
        ssh_shell.send("commit \n")
        time.sleep(1)
        output = ssh_shell.recv(9600)
        print("output" + output)
        x=x+1
    else:
        print("server +tip+ is down")  
	  