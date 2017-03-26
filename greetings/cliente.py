#!/usr/bin/env python

# adaptado de https://wiki.python.org/moin/TcpCommunication

import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = ''

for i in range(1, len(sys.argv)):
    MESSAGE += sys.argv[i]
    MESSAGE += ' '

if(len(MESSAGE) < 1):
    MESSAGE = "você não inseriu o nome na linha de comando"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data.decode())
