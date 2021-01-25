# Name: Vivian Feng and Shriya Muthukumar
# Date: 2.28.2020

from math import ceil


def encrypt(message):
    i = 0
    # message = message.upper()
    # message = message.replace(' ', '#')
    firstLine = ""
    secondLine = ""
    while i < len(message):
        if i % 2 == 1:
            secondLine += message[i]
        else:
            firstLine += message[i]
        i += 1

    encryptedMessage = firstLine + secondLine

    return encryptedMessage


def decrypt(message):
    lenFirst = int(ceil(len(message) / 2.0))
    lenSecond = len(message) - lenFirst

    firstStr = message[0:lenFirst]
    secondStr = message[lenFirst:]

    if lenFirst != lenSecond:
        secondStr += " "

    chars = zip(firstStr, secondStr)
    decryptedMessage = ""
    for tup in chars:
        decryptedMessage += (tup[0] + tup[1])

    return decryptedMessage


choice = raw_input("Would you like to encrypt or decrypt a message\n(encrypt: e, decrypt: d): ")

message = raw_input("Enter your message: ")

if choice == 'e':
    print "Your encrypted message: ", encrypt(message)

else:
    print "Your decoded message: ", decrypt(message)
