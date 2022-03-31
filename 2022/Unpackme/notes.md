# Rev

# Flag:

Can you get the flag? Reverse engineer this binary.

upx -d unpackme-upx -o unpacked

gdb unpacked

disas *main
...
0x0000000000401ef8 <+133>:   cmp    eax,0xb83cb
...

0xb83cb = 754635

./unpacked 
What's my favorite number? 754635
picoCTF{up><_m3_f7w_e510a27f}