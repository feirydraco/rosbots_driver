import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.0.12', 9999))
while(1):
    m = s.recvfrom(4096)
    print(m)
