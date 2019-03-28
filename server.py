import socket
import sys

#stores the key and a specified value on the server
def POSTHandler(key, value):
    mapper[key] = value

#returns the value of the key
def GETHandler(key):
    return mapper[key]

#lists all of the key value pairs
def DUMPHandler():
    return mapper

mapper = {}
port = 12345

s = socket.socket()
s.bind(('127.0.0.1', port))
s.listen(10)

c, addr = s.accept()

req  = c.recv(1024).decode('ascii')

print(req)

c.close()

# while True:
#     s2, anything = s.accept()

#     request = c.recv(2029).decodea('ascii')
#     request = request.split(':')

#     print(request)

#     if request[0] == 'PUT':
#         PUTHandler(request[1], request[2])
#         s2.send('PUT request sent')
#     elif request[0] == 'GET':
#         response = GETHandler(request[1])
#         s2.send(res.encode('utf-8'))
#     elif request[0] == 'DUMP':
#         response = DUMPHandler()
#         s2.send(res.encode('utf-8'))

#     s2.close()
