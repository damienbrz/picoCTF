# Web

# Flag: picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb} 

Can you get the flag? Go to this website and see what you can discover.

http://saturn.picoctf.net:63115/

Login page

```
Secure Customer Portal

Only letters and numbers allowed for username and password.

[Username][Password][Submit]
```

If you submit the page with random credentials while the network tab of developer tools is open, you can see it's loading a file called `secure.js`

secure.js
```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

Submit these creds and the flag appears