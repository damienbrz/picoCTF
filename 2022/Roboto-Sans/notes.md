# Web

# Flag: picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}

The flag is somewhere on this web application not necessarily on the website. Find it. Check this out.

http://saturn.picoctf.net:51108/

Source doesn't show much.

Looked into the fonts files (due to the challenge name), nothing

Ran `wget -m http://saturn.picoctf.net:51108/`

Saw the robots.txt file being downloaded

```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

```
echo -n 'anMvbXlmaWxlLnR4dA==' | base64 -d                                
js/myfile.txt
```

Visiting http://saturn.picoctf.net:51108/js/myfile.txt

We get the flag picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
