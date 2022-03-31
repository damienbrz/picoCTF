# For

# Flag: picoCTF{nc_73115_411_dd54ab67}

Stream 0 has the following conversation

```
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable
```

Using the filter `tcp.stream eq 2` we can save the data as `file.des3` in `raw` mode as it occured on port 9002

Run `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`