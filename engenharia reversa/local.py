passos = """wwaawwwwwwwwwdwwwwawwwwww"""


array = """WWAAWWWWWWWWWDWWWWAWWWWWWSSSSSSDSSSSASSSSSSAAASAAAAAASAAAASAAAADDDDWDDDDWWWAWWAAAAAWADWWWWWWAWAWWWWWAAWW"""

array_esoj = ['w', 'w', 'a', 'a', 'w', 'w', 'w', 'a', 'a', 'd', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'd', 'w', 'w', 'w', 'w', 'a', 'w', 'w', 'w', 'w', 'w', 'w', 's', 's', 's', 's', 's', 's', 'd', 's', 's', 's', 's', 'a', 's', 's', 's', 's', 's', 's', 'a', 'a', 'a', 's', 'a', 'a', 'a', 'a', 'a', 'a', 's', 'a', 'a', 'a', 'a', 's', 'a', 'a', 'a', 'a', 'd', 'd', 'd', 'd', 'w', 'd', 'd', 'd', 'd', 'w', 'w', 'w', 'a', 'w', 'w', 'a', 'a', 'a', 'a', 'a', 'w', 'a', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'a', 'w', 'a', 'w', 'w', 'w', 'w', 'w', 'a', 'a', 'w', 'w']

nome = "trusting_nobel x"

#pip3 install pwntools
from pwn import *
p = process("./game2")
a = input()
print(p.recvline()) #whats you name
p.sendline(b"trusting_nobel x")
#p.sendline(b"0291-3076-5273-1111")



for letter in array:
    p.sendline(letter.lower())
p.interactive()
#p.sendline("b")
#p.sendline("b")
#p.sendline("b")
#p.sendline("a")


# aleatorios = [4, 3, 6, 6, 4, 1, 4, 2, 5, 1, 3, 3, 6, 4, 5, 3, 1, 3, 5, 1]

#aleatorios = [2,1, 1, 6, 4, 4, 4, 6, 4, 4, 2, 1, 5, 5, 1, 6, 1, 1, 5, 6]

#aleatorios =   [2, 6, 4, 1, 5, 2, 1, 5, 3, 6, 3, 3, 4, 6, 1, 3, 2, 6, 1, 1]
                # 2 6 4 1 5 2 1 5 3 6 3 3 4 6 1 3 2 6 1 1 


# a --> ataque
# b --> defende

"""
while(contador != 2):
    if aleatorios[c] == 6:
        p.sendline('a')
        contador = contador + 1
    else:
        p.sendline('b')
    if c == len(aleatorios)-1:
        c = 0
    c = c + 1
"""