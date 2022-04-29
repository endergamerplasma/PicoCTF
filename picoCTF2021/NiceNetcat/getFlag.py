with open("ASCII.txt", "r") as f:
    chars = [chr(int(i.strip())) for i in f.readlines()]
    print("".join(chars))
