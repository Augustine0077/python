import random
import string
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars =  list(chars)
keys = chars.copy()
random.shuffle(keys)
# print(f"chars: {chars}")
# print(f"keys: {keys}")



#encryption program
plain_text = input("Enter text to encrypt: ")
chipher_text = ""

for letter  in plain_text:
    index = chars.index(letter)
    chipher_text += keys[index]

print(f"original text: {plain_text}")
print(f"chipher text: {chipher_text}")

#decryption program

chipher_text = input("Enter text to decrypt: ")
plain_text = ""

for letter  in chipher_text:
    index = keys.index(letter)
    plain_text += chars[index]


print(f"chipher text: {chipher_text}")
print(f"original text: {plain_text}")