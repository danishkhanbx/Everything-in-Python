import socket

# A socket is one endpoint of a two-way communication link between two programs running on the network.
# It is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.
# An endpoint is a combination of an IP address and a port number.

s = socket.socket()  # creating a socket itself, and the default address will be ipv4 & the type of network will be TCP
print('Socket Created')

# binding socket with a machine(if different machines than add the ip address of that machine instead of localhost)
s.bind(('localhost', 9999))  # and a port number of 9999(available, free, & unused). Port number ranges between 0-65535

# listening to the clients for some command, message or request.
s.listen(3)  # max 3 clients at a time, if another client request comes it will be getting refused
print('waiting for connections...')

while True:  # it will continuously accept requests until buffer the is full
    c, address = s.accept()  # accepting the client socket and clients address
    name = c.recv(1024).decode()  # 1024 is the buffer size(temporary memory), decode will print in strings not in bytes
    print('Connected with', address, name)  # port number and name of client
    c.send(bytes('Welcome Home', 'utf-8'))
    c.close()  # closing the connection, when the client exits
