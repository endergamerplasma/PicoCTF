import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = ""
key_part_static3_trial = "}"

username_trial = b"ANDERSON"

hashIndices = [4, 5, 3, 6, 2, 7, 1, 8]
username_hash = hashlib.sha256(username_trial).hexdigest()
for i in hashIndices:
    key_part_static2_trial += username_hash[i]

key = key_part_static1_trial + key_part_static2_trial + key_part_static3_trial
print(key)
