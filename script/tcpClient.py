import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    pesan = raw_input("->")
    while pesan != 'q':
        s.send(pesan)
        data = s.recv(10214)
        print 'Received from server :' + str(data)
        pesan = raw_input("->")
    s.close()
if __name__ == '__main__':
    Main()

