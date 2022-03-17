import socket

s = socket.socket()     # create a socket object
host = socket.gethostname()     # get local host name
port = 11000    # designate port
s.bind((host, port))    #bind host to port

s.listen(5)     # wait for connection
while True:
    c, addr = s.accept()    # establish connection with client
    print("connection inbound from: ", addr)    # print client address
    message = bytes("Connected Successfully!", 'utf-8')
    c.send(message)   # send string to client
    c.close()   # close connection