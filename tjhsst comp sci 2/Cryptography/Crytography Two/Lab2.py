# Name: Vivian Feng and Shriya Muthukumar
# Date: 3.4.2020

import string

alpha = list(string.ascii_uppercase)
cipher = []

for index in range(len(alpha)):

    transposedIndex = index + 13
    if transposedIndex > len(alpha) - 1:
        transposedIndex -= (len(alpha))

    cipher.append(alpha[transposedIndex])


def encrypt(message):
    global cipher, alpha
    message.upper()
    encryptedMessage = ""
    for char in message:
        if char in alpha:
            replacement = alpha.index(char)
            char = cipher[replacement]
        encryptedMessage += char

    return encryptedMessage


def decrypt(message):
    global cipher, alpha
    message.upper()
    decryptedMessage = ""
    for char in message:
        if char in cipher:
            replacement = cipher.index(char)
            char = alpha[replacement]
        decryptedMessage += char

    return decryptedMessage


print encrypt("THE END IS NEIGH")
