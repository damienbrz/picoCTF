import string

subs = "QWITJSYHXCNDFERMUKGOPVALBZ"
chars = string.ascii_uppercase

enc = "mxirIOS{5PW5717P710E_3V0DP710E_03055505}".upper()
dec = ""
for c in enc:
  if subs.find(c) >= 0:
    dec += chars[subs.find(c)]
  else:
    dec += c
print(dec)