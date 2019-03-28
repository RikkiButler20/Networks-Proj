import socket
import sys

mapper = {}

#stores the key and a specified value on the server
def PUTHandler(key, value):
    mapper[key] = value

#returns the value of the key
def GETHandler(key):
    if key in mapper:
            return mapper[key]
    return 'key does not exist'

#lists all of the key value pairs
def DUMPHandler():
    if not mapper:
        return {}
    return mapper

port = 11112

s = socket.socket()
s.bind(('127.0.0.1', port))
s.listen(10)

while True:
    s2, anything = s.accept()

    request = s2.recv(2029).decode('ascii')
    request = request.split(':')

    print(request)

    if request[0] == 'PUT':
        PUTHandler(request[1], request[2])
        s2.send(b'PUT request sent')
    elif request[0] == 'GET':
        response = GETHandler(request[1])
        s2.send(response.encode('utf-8'))
    elif request[0] == 'DUMP':
        mapper = str(mapper)
        response = DUMPHandler()
        if response:
            s2.send(response.encode('utf-8'))
        else:
            s2.send(b'there is nothing to dump')


    s2.close()
