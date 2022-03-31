# Crypt

# Flag: picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_5E3C2EE2}

Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. Can you figure out the contents of the message? Download the message here. Wrap your decrypted message in the picoCTF flag format.

```
python3 decrypt.py
Publicly Shared Variables:
    Publicly Shared Prime:  13
    Publicly Shared Base:   5

  Alice Sends Over Public Chanel:  8
Bob Sends Over Public Chanel:  8

------------

Privately Calculated Shared Secret:
    Alice Shared Secret:  5
    Bob Shared Secret:  5
```

The shared secret is 5

We can use this on the caesar cipher shift
https://www.dcode.fr/caesar-cipher