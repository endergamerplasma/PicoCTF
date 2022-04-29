from binascii import unhexlify

stackDump = "826f390-804b000-80489c3-f7f4fd80-ffffffff-1-826d160-f7f5d110-f7f4fdc7-0-826e180-a-826f370-826f390-6f636970-7b465443-306c5f49-345f7435-6d5f6c6c-306d5f79-5f79336e-35343036-64303664-ffbe007d-f7f8aaf8-f7f5d440-bea45500-1-0-f7decce9-f7f5e0c0-f7f4f5c0-f7f4f000-ffbe9bd8-f7ddd68d-f7f4f5c0"
flag = ""
for hexWord in stackDump.split("-"):
    word = ""
    for i in range(0, len(hexWord), 2):
        try:
            word += unhexlify(hexWord[i:i+2]).decode()
        except:
            pass
    flag += word[::-1]

flag = flag[flag.find("picoCTF"):]
flag = flag[:flag.find("}")+1]
print(flag)
