import sys
import socket

host = "localhost" # Can also be set to IP of target computer
port = 13000
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input("> ")
    sock.sendto(data, addr)
    if data == "exit":
        break

sock.close()
sys.exit(0)
