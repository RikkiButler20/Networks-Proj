import socket
import sys

cached_mapper = {}

def requestServer(request):
    s = socket.socket()
    port 11112

    s.connect(('127.0.0.1', port))
    s.sendall(request.encode('utf-8'))

    response = str(s.recv(2029))
    response = response[2:-1]

    return response


while True:
    s2, anything = s.accept()

    request = s2.recv(2029).decode('ascii')
    request = request.split(':')

    print(request)

    # if put request, send to server
    if request[0] == 'PUT':
        requestServer(':'.join(request))
        s2.send(b'PUT request received')
    #if get request
    elif request[0] == 'GET':
        #check if in cached hashmap
        if request[1] in cached_mapper:
            s2.send(cached_mapper[request[1]].encode('utf-8'))
        #if not then get value and put in cached hashmap
        else:
            response = requestServer(':'.join(request))
            cached_mapper[request[1]] = str(response)
            s2.send(cached_mapper[request[1]].encode('utf-8'))
    #if dump, send to server
    elif request[0] == 'DUMP':
        response = requestServer(':'.join(request))
        s2.send(response.encode('utf-8'))


    s2.close()

