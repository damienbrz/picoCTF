# Web

# Flag: picoCTF{gr4d3_A_c00k13_65fd1e1a}

Can you get the flag? Go to this website and see what you can discover.

http://saturn.picoctf.net:52021/

```
Online Gradebook
[Button]
```

When click the button it calls `continueAsGuest()`

guest.js
```
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

On click we go to http://saturn.picoctf.net:52021/check.php

Check the cookies and we have `isAdmin=0` so wif we change that to 1 we get the flag