#!/usr/bin/python

from socket import *
from time import ctime
import os
import logging
import commands


HOST=''
PORT=2222
BUFSIZ=1024
ADDR=(HOST,PORT)

logger = logging.getLogger('mytool')
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('/tmp/output.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection....')
    tcpCliSock,addr=tcpSerSock.accept()
    print('connected from:',addr)

    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if data:
            status,output=commands.getstatusoutput('yum install -y  %s' %data) 
            if status==0:
                tcpCliSock.send('%s have installed' %data)
                logger.info('%s have been installed' %data)
            else:
                tcpCliSock.send(output)
                logger.warning(output)
            break
#        tcpCliSock.close()

#        if not data:
#            break
#        tcpCliSock.send('[%s] %s' %(ctime(),data))
#                tcpCliSock.close()

#tcpSerSock.close()