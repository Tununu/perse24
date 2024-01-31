pw1 = input()
pw2 = input()
pw3 = input()

if pw1 == pw2:
  if pw1 == pw3:
    print('OK')
  else:
    print('ENTRY 3 MISMATCH')
else:
  if pw1 == pw3:
    print('ENTRY 2 MISMATCH')
  else:
    print('BOTH MISMATCH')
