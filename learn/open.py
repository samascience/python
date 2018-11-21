import paramiko
import time
import socket 
import sys 

ip="10.255.7."
ip1="10.137.11."
True=1
x=2

while True:
	tip = ip+str(x) 
	tip1=ip1+str(x)
	print(tip)
	#This goes for a infinite loop if the ip is not reachable. You are incrementiing
	#"x" only when the device is reachable
	rep=os.system('ping' + tip)
	#below line will have error because of the indentation. edit it please 
	if rep == 0:
		print "switch is up"
		time.sleep(10)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect("tip", username="root", password="default")
		ssh_shell = ssh.invoke_shell()
		ssh_shell.send("config -s config.interfaces.wan.mode=static \n" )
		ssh_shell.send("config -s config.interfaces.wan.address="+tip1+"\n" )
		ssh_shell.send("config -s config.interfaces.wan.netmask=255.255.254.0 \n" )
		ssh_shell.send("config -s config.interfaces.wan.dns1=10.137.10.1  \n" )
		ssh_shell.send("config -s config.interfaces.wan.gateway=192.168.1.1 \n")
		ssh_shell.send("config -r ipconfig \n" )
		#Add the below line outside if/else to avoid the infinite loop
		x=x+1
		time.sleep(5)
		output = ssh_shell.recv(9600)
		print "output" + output
	else:
		print "server +tip+ is down"
# You will never hit the below conditon.. You can remove the below condition.. No elsecondition for while loop
else : 
	print("loop exited")	

#1. You dont have an option to get the input from the user. You need to use raw_input() as discussed yesterday to get the input from user\
#2. Get the oinput from user to check if he wants to continue/not. based on that set the value of the variable "True" so that while will not be infinite always
#3. Try adding the functions to this and you need to call it in a main() function. "main()" is required in every function adn they will check that in interviews/reviews
#4. This is all i can think of now. Best of luck changing the above comments. :P Laptop battery is low.. connect to power
#5. since you are using the only function "sleep" from the package time, import it as "from time import sleep". you can use "sleep()" instead of time.sleep(). This will help in importing only the fucntion you 
#are using instead of the complete package

