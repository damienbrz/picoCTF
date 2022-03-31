# Web

# Flag:  picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}

Can you get the flag? Here's the website. We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?

http://saturn.picoctf.net:56978/

```
Web eReader

..
divine-comedy.txt
oliver-twist.txt
the-happy-prince.txt
[Input][Submit]
```

If we submit `../../../../../../../flag.txt` it reads the flag file