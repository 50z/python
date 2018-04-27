import socket
s = socket.socket()

host = socket.gethostname()
#host = 172.25.3.112
port = 1234
s.bind((host,port))

s.listen(5)

while True:

        c, addr = s.accept()
        print('Got connection from', addr)
        msg = 'Thank you for connecting'
        c.send(msg.encode('utf-8'))
        c.close()