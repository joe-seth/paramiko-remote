"""
You will need to ssh into the remote machine and if you have appropriate credentials, you can invoke the shell scripts.
For using ssh, you can easily use paramiko module that provides ssh automation
    http://www.lag.net/paramiko/
A typical example:
"""
import paramiko
import sys
import os
import os.path
passwd = ""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('servername', username, password=passwd)
stdin, stdout, stderr = ssh.exec_command('df -h')
x = stdout.readlines()
print(x)
for line in x:
    print(line)
ssh.close()