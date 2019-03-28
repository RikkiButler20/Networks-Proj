import socket

def send_GET(s, key):
    request = 'GET: '+key
    s.sendall(request.encode('utf-8'))
    print(s.recv(2029))
def send_PUT(s, key, value):
    request = 'PUT: ' + key + ": " + value
    s.sendall(request.encode('utf-8'))
    print(s.recv(2029))
def send_DUMP(s):
    request = 'DUMP'
    s.sendall(request.encode('utf-8'))
    print(s.recv(2029))


def operationCommands():
    while True:
        print("Connected")
        s = socket.socket()

        port = 12345
        
        s.connect(('127.0.0.1', port))
        
        # s.sendall(b'anything')

        commands = input("GET key, PUT key value, DUMP, or Q (quit): ")
        commands = commands.split(' ')
        op = commands.pop(0)
        if op.upper() == "GET":
            key = commands.pop(0)
            send_GET(s,key)
        elif op.upper() == "PUT":
            key = commands.pop(0)
            value = ''.join(commands)
            send_PUT(s, key, value)
        elif op.upper() == "DUMP":
            send_DUMP(s)
        elif op.upper() == 'Q':
            print('quit')
            break
        else:
            print('Invalid. Try again.')
        
        s.close()

operationCommands()
# s = socket.socket()

# port = 12345

# s.connect(('127.0.0.1', port))
# s.sendall(b'anything')

# s.close()