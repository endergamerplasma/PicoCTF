encryptedFlag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
flag = ''

for i in encryptedFlag:
    if not i.isalpha():
        flag += i
    elif ord(i) >= ord('a'):
        flag += chr(((ord(i) - ord('a') + 13) % 26) + ord('a'))
    else:
        flag += chr(((ord(i) - ord('A') + 13) % 26) + ord('A'))

print(flag)
