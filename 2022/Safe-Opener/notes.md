# Rev

# Flag: picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

Compile the program
```
javac SafeOpener.java
```

The source code:

```
Base64.Encoder encoder = Base64.getEncoder();
key = keyboard.readLine();
encodedkey = encoder.encodeToString(key.getBytes());
```

This is a simple base64 encoder.

This is how we compare the key
```
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";        
if (password.equals(encodedkey) {
    ...
}
```

Decode
```
echo -n "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d                
pl3as3_l3t_m3_1nt0_th3_saf3
``

Test and run the program
```
java SafeOpener  
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter password for the safe: pl3as3_l3t_m3_1nt0_th3_saf3
cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz
Sesame open
```

