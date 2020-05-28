import socket
import datetime
import json

if __name__ == '__main__':
    port = 123
    ip = '127.0.0.1'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    with open('time.conf') as file:
        seconds = json.load(file)['seconds']
    print('Server started')
    print(f'Loaded seconds: {seconds}')
    while True:
        data, addr = sock.recvfrom(512)
        print(f'Data came from {addr}')
        current_time = datetime.datetime.now()
        print(f'Actual time: {current_time}')
        lied_time = current_time + datetime.timedelta(0, seconds)
        print(f'Lied time: {lied_time}')
        sock.sendto(bytes(str(lied_time), encoding='utf8'), addr)
