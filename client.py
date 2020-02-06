#coding=utf-8

import socket

host = '192.168.31.18'
port = 11111

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((host,port))
data = c.recv(1024).decode()
print(data)
data = input('Please write down a data to send to the remote server:').encode()
c.send(data)
