import base64
import paramiko
import sys

dir_test= []
def ssh_conn():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.1.9', username='ssh_server', password='mypassword')

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(
            'ss -ltn')
    
    for line in ssh_stdout:
        dir_test.append(line.strip('\n'))



ssh_conn()

for i in dir_test:
    print(i.strip())

sys.exit()

