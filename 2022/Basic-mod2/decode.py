import string

numbers = [104, 85, 69, 354, 344, 50, 149, 65, 187, 420, 77, 127, 385, 318, 133, 72, 206, 236, 206, 83, 342, 206, 370]

letters = " " + string.ascii_lowercase + string.digits + "_"

flag = ""

for value in numbers:
  flag += letters[pow(value, -1, 41)]

print(f"picoCTF{{{flag}}}")