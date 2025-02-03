# 1.0

# Enter message that is encrypted
# return encrypted message
# decrypt message and return it

# key value pairs
encrypt_key = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
    'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a', 'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
    'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'
}

decrypt_key = {
    'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j',
    'w': 'k', 'x': 'l', 'y': 'm', 'z': 'n', 'a': 'o', 'b': 'p', 'c': 'q', 'd': 'r', 'e': 's', 'f': 't',
    'g': 'u', 'h': 'v', 'i': 'w', 'j': 'x', 'k': 'y', 'l': 'z'
}

def encrypt_message(message):
    encrypted = []
    for char in message: # iterate over original message.
        iteration  = encrypt_key.get(char, char) # if it's a known letter, we input its key into the dictionary and return its value.
        encrypted.append(iteration) # we take this new encrypted letter and add it to the list.
    return_encrypted = "".join(encrypted) # we then unpack the list to convert it to a normal string.
    return return_encrypted # we now print the encrypted message.

def decrypt_message(encrypt_key):
    decrypted = []
    for char in encrypt_key:
        iteration = decrypt_key.get(char, char)
        decrypted.append(iteration)
    return_decrypted = "".join(decrypted)
    return return_decrypted

# user inputted message
message = input("> ")
encrypted = encrypt_message(message)
decrypted = decrypt_message(encrypted)

print(f"encrypted: {encrypted}")
print(f"decrypted: {decrypted}")