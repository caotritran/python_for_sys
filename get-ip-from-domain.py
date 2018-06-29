import sys
import socket

if len(sys.argv) > 1:
    hostname = sys.argv[1]
    ip = socket.gethostbyname(hostname)
    print(ip)
else:
    print("usage: ex4.py domain_name")
