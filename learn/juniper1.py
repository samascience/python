import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.205.18.22", username="root", password="root123")
ssh_shell = ssh.invoke_shell()
ssh_shell.send("cli \n" )
ssh_shell.recv(1000)
ssh_shell.send("show vlans | no-more \n")
time.sleep(5)
output = ssh_shell.recv(9600)
print "output" + output
