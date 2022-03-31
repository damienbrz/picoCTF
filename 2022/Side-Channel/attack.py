from pwn import *
import time

valid = ""

for pos in range(0, 8):
  speed = 0
  val = 0
  for i in range(0, 10):
    p = process('./pin_checker')
    print(p.recvline())
    pin = f"{valid}{i}{'0' * (7 - pos)}\n".encode()
    print(f"Sending pin: {pin}")
    start = time.time()
    p.write(pin)
    print(p.readall())
    end = time.time()
    duration = (end-start)
    if duration > speed:
      speed = duration
      val = i
  valid += f"{val}"
  print(f"Valid: {valid}")
print(f"Final pin: {valid}")
