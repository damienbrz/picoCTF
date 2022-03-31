# Rev

# Flag: picoCTF{d3bugg3r_dr1v3_72bd8355}

$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)