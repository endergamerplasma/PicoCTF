from pwn import * 


KEY_LEN = 50000
CHUNK = 5000

r = remote("mercury.picoctf.net", 11188)
r.recvuntil("This is the encrypted flag!\n")
hexFlag = r.recvlineS(keepends=False)
binFlag = unhex(hexFlag)

p = log.progress('count')
count = KEY_LEN - len(binFlag)
while count > 0:
    p.status(str(count))
    chunkSize = min(count, CHUNK)
    r.sendlineafter("What data would you like to encrypt? ", "a"*chunkSize)
    count -= chunkSize

p.status(str(count))
r.sendlineafter("What data would you like to encrypt? ", binFlag)
r.recvlineS()
flag = f"picoCTF{{{unhex(r.recvlineS()).decode('ascii')}}}"
print(flag)
