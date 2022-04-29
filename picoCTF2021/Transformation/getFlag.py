with open("enc", "r") as f:
    encodedFlag = f.read().strip()
    flag = ""
    for i in encodedFlag:
        flag += chr((ord(i)-(ord(i)&255)) >> 8)
        flag += chr(ord(i)&255)

print(flag)
