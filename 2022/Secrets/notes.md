# Web

# Flag: picoCTF{succ3ss_@h3n1c@10n_51b260fe}

We have several pages hidden. Can you find the one with the flag? The website is running here.

http://saturn.picoctf.net:50167/index.html

Source
```
<img
    src="secret/assets/DX1KYM.jpg"
    alt="https://www.alamy.com/security-safety-word-cloud-concept-image-image67649784.html"
    class="responsive"
/>
```

Then visitising http://saturn.picoctf.net:50167/secret/

Source
```
<link rel="stylesheet" href="hidden/file.css" />
```

Then visitising http://saturn.picoctf.net:50167/secret/hidden/

Source
```
<input type="hidden" name="db" value="superhidden/xdfgwd.html" />
```

Then visitising http://saturn.picoctf.net:50167/secret/hidden/superhidden/

Source
```
<h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_51b260fe}</h3>
```