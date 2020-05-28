import socket

if __name__ == '__main__':
    port = 51126
    ip = '127.0.0.1'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    sock.sendto(b'', (ip, 123))
    print('Sent data')
    data, addr = sock.recvfrom(512)
    print(data.decode(encoding='utf8'))
