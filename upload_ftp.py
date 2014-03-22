#!/usr/bin/env python
'''this is module use to learn paramiko.
   the function is use to upload file'''
import paramiko
hostname = 'hostip'
username = 'username'
password = 'pass'
port = 22
paramiko.util.log_to_file('1.txt')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname = hostname,port=port,username=username,password=password)
stdin,stdout,stderr=s.exec_commadn('free;df -h')
print stdout.read()
s.close()
