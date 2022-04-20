import base64

s = 'vJqfip28ioydips='
base = base64.b64decode(s)

for i in base:
    i = ~i & 255
    i = i ^ 16
    print(chr(i),end='')
print()