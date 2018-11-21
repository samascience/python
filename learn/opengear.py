import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.0.1", username="root", password="default")
ssh_shell = ssh.invoke_shell()
ssh_shell.send("config -s config.interfaces.wan.mode=static \n" )
ssh_shell.send("config -s config.interfaces.wan.address=10.255.7.51 \n" )
ssh_shell.send("config -s config.interfaces.wan.netmask=255.255.254.0 \n" )
ssh_shell.send("config -s config.interfaces.wan.dns1=10.255.6.1 \n" )
ssh_shell.send("config -r ipconfig \n" )

time.sleep(5)
output = ssh_shell.recv(9600)
print "output" + output