import string

numbers = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397]

letters = string.ascii_uppercase + string.digits + "_"

flag = ""

for value in numbers:
  flag += letters[value % 37]

print(f"picoCTF{{{flag}}}")