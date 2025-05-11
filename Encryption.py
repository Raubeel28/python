import random
import string

chars = string.punctuation+ string.ascii_letters+string.digits+" "
chars = list(chars)
key = chars.copy()
random.shuffle(key)



#print(f"chars : {chars}")
#print(f"key : {key}")
# encryption
plaintext = input("Enter a message to ecrypt:  ")
cipher = ""
for letter in plaintext:
    index = chars.index(letter)
    cipher += key[index]
print (f"original message : {plaintext}")
print (f"ecryptedd message : {cipher}")

#decryption

cipher = input("Enter a message to decrypt:  ")
plaintext= ""
for letter in cipher:
    index = key.index(letter)
    plaintext += chars[index]

print (f"ecryptedd message : {cipher}")

print (f"original message : {plaintext}")

