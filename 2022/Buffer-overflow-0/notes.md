# Exp

# Flag: picoCTF{ov3rfl0ws_ar3nt_that_bad_34d6b87f}

Smash the stack Let’s start off simple, can you overflow the correct buffer?

The code defines a `sigsegv_handler` function thaat is called upon segfault

The vuln function do a `strcopy` from a buffer of a size of 100 int oa 16 char size.

Make the input long enough and it will segfault

nc saturn.picoctf.net 65355
Input: hhkfserfhsdfhusdhfjhsdahfghsdgfgsadkfgsdafsdafsadfa
picoCTF{ov3rfl0ws_ar3nt_that_bad_34d6b87f}