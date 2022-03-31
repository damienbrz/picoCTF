# For

# Flag: picoCTF{t1m1ng_4tt4ck_eb4d7efb}

There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? Download the PIN checker program here pin_checker Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using nc saturn.picoctf.net 52680 and provide it the PIN to get your flag.

Time based attack

```
python attack.py
...
Sending pin: b'48390513\n'
[+] Receiving all data: Done (86B)
[*] Process './pin_checker' stopped with exit code 1 (pid 448497)
b'8\nChecking PIN...\nAccess granted. You may use your PIN to log into the master server.\n'
...
```