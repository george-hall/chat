import sys
import socket

host = ""
port = 13000
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

print "Waiting to receive messages..."

while True:
    (data, addr) = sock.recvfrom(buf)
    print "Received message: " + data
    if data == "exit":
        break

sock.close()
sys.exit(0)
