# Encryption program
# Cyber Security program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
#Now we are going to shuffle this key:
random.shuffle(key)
# print(chars)
# print(key)

# Encryption'
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)  # esma chai chars list bata position nikalcha
    cipher_text += key[index]    #tespachi chai key list ko chai nikaleko position ma jun character cha tes bata encrypt gardincha
    
print(f"Original message: {plain_text}")
print(f"Encryption: {cipher_text}")

# Decryption:
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)  # number aucha position
    plain_text += chars[index]
    
print(f"Original message: {cipher_text}")
print(f"Decryption: {plain_text}")