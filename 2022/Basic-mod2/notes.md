# Crypt

# Flag: picoCTF{1nv3r53ly_h4rd_dadaacaa}

A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})


Given two integers ‘a’ and ‘m‘, find modular multiplicative inverse of ‘a’ under modulo ‘m’.
The modular multiplicative inverse is an integer ‘x’ such that. 

a x ≅ 1 (mod m)


```
python3 decode.py
```