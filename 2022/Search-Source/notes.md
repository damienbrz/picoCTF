# Web

# Flag: 

The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is here

http://saturn.picoctf.net:50761/

Looking at the source code

```
<!-- six_box
end six_box   The flag is not here but keep digging :)-- >
```

Let's keep digging

View source of style.css and search for picoCTF

```
.navbar-expand-md .navbar-nav .nav-link {
     padding: 15px 48px;
     font-size: 16px;
     color: #000;
     line-height: 18px;
}
/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
```

### Note

You can download the site with  `wget -m http://saturn.picoctf.net:50761/` to search the whole source locally.