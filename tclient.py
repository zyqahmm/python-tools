#!/usr/bin/python

from socket import *

HOST='aa'
PORT=2222
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=raw_input('>')
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()