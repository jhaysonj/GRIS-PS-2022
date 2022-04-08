passos = """wwaawwwwwwwwwdwwwwawwwwww"""


array = """WWAAWWWWWWWWWDWWWWAWWWWWWSSSSSSDSSSSASSSSSSAAASAAAAAASAAAASAAAADDDDWDDDDWWWAWWAAAAAWADWWWWWWAWAWWWWWAAWW"""

array_esoj = ['w', 'w', 'a', 'a', 'w', 'w', 'w', 'a', 'a', 'd', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'd', 'w', 'w', 'w', 'w', 'a', 'w', 'w', 'w', 'w', 'w', 'w', 's', 's', 's', 's', 's', 's', 'd', 's', 's', 's', 's', 'a', 's', 's', 's', 's', 's', 's', 'a', 'a', 'a', 's', 'a', 'a', 'a', 'a', 'a', 'a', 's', 'a', 'a', 'a', 'a', 's', 'a', 'a', 'a', 'a', 'd', 'd', 'd', 'd', 'w', 'd', 'd', 'd', 'd', 'w', 'w', 'w', 'a', 'w', 'w', 'a', 'a', 'a', 'a', 'a', 'w', 'a', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'a', 'w', 'a', 'w', 'w', 'w', 'w', 'w', 'a', 'a', 'w', 'w']

nome = "trusting_nobel x0"

#pip3 install pwntools
from pwn import *
p = remote("35.184.230.50",3000)
print(p.recvline()) #whats you name
p.sendline(b"trusting_nobel777682877416")
p.sendline(b"0291-3076-5273-1111")



for letter in array:
    p.sendline(letter.lower())

for c in range(5):
    p.sendline(b"a")
p.interactive()
