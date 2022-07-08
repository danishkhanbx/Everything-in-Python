import socket

c = socket.socket()
c.connect(('localhost', 9999))  # server will bind the port, client will simply connect(ip address, port number) with it
name = input('Enter your name: ')
c.send(bytes(name, 'utf-8'))  # sending clients name in utf format
print(c.recv(1024).decode())
