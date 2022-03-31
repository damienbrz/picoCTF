enc = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

count = 3

message = ""

for chars in range(0, len(enc), count):
  message += enc[chars+count - 1] + enc[chars:chars+count -1]
print(message)