import paramiko
import time
x=2
ip="10.255.7."
True=1

while True:
	uip=raw_input("Please enter the ip address you want to assign: ")
	print(uip)
	choice=raw_input("Enter 1 to decrement and 0 to increment: ")
	if choice == "1" :
		x=x-1
		print("\n"+ip+str(x)+"\n")
	else:
		x=x+1
		print("\n"+ip+str(x)+"\n")
		
	

#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(ip+x, username="root", password="default")
#ssh_shell = ssh.invoke_shell()
#ssh_shell.send("config -s config.interfaces.wan.mode=static \n" )
#ssh_shell.send("config -s config.interfaces.wan.address="+uip+"\n" )
#ssh_shell.send("config -s config.interfaces.wan.netmask=255.255.254.0 \n" )
#ssh_shell.send("config -s config.interfaces.wan.dns1=10.255.6.1 \n" )
#ssh_shell.send("config -r ipconfig \n" )

time.sleep(5)
#output = ssh_shell.recv(9600)
#print "output" + output