import paramiko

import sys

results = []

def ssh_conn():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.1.9',username= 'ssh_server')


    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('mkdir paramiko_test')
 
    for line in ssh_stdout:
        results.append(line.strip('\n'))


ssh_conn()

for i in results:
    print(i.strip())


#sys.exit()


