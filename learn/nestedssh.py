import paramiko
import time


spine_mgmt_ip = "10.137.1.1"
spine = paramiko.SSHClient()
spine.set_missing_host_key_policy(paramiko.AutoAddPolicy())
spine.connect(spine_mgmt_ip, username='root', password='Apples!234')
print("Success SSH to spine!")

leaf_mgmt_ip_prefix = "10.201.0."
i = 11

while (i < 15) :
    leaf_mgmt_ip = leaf_mgmt_ip_prefix + str(i)
    spine_transport = spine.get_transport()
    dest_addr = (leaf_mgmt_ip, 22)
    src_addr = (spine_mgmt_ip, 22)
    spine_channel = spine_transport.open_channel("direct-tcpip", dest_addr, src_addr)

    leaf = paramiko.SSHClient()
    leaf.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    leaf.connect(spine_mgmt_ip, username='root', password='Apples!234', sock=spine_channel)
    print("Success SSH to leafs!")

    print("Before CLI")
    stdin, stdout, stderr = leaf.exec_command("cli \n")
    print("Before show version")
    stdin, stdout, stderr = leaf.exec_command("show version \n")
    print(stdout.read())
    print("after show version")
    leaf.close()
    i = i+1
spine.close()
