# Rev

# Flag: picoCTF{175_chr157m45_cd82f94c}

Adding a 
```
print(plain.decode())
```

at the end of the program and running it

```
python3 unpackme.flag.py
What's the password? test
That password is incorrect.

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_cd82f94c}')
else:
  print('That password is incorrect.')
```