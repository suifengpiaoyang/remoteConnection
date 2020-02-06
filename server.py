#!/usr/bin/python
#coding=utf8

import socket

host = ''
port = 11111
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print('Waiting for connection...')

while True:
    server,address = s.accept()
    print('Connect from {}'.format(address))
    server.send('CangLaoShi'.encode())
    data = server.recv(1024).decode()
    print('Recv {} from {}'.format(data,address))

