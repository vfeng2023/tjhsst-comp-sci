# Name: Vivian Feng and Shriya Muthukumar
# Date: 3/11/2020

import random
import string

# create code pad with certain number of lines and write to file
numLines = 100
alphabetList = list(string.ascii_uppercase)
# each line will contain 26 letters the message is encrypted by going to the line corresponding to the position of
# the letter in the message and the position of letter in the line is the same as the position in the message, cycling every 26 lines
oneTimePad = open('pad.txt', 'w')
for line in range(numLines):
    newLine = "".join(random.sample(alphabetList, len(alphabetList)))
    oneTimePad.write(newLine + "\n")
    print newLine
oneTimePad.close()


# encryption
def encrypt(plaintext, OTPName):
    global alphabetList
    # read pad as list
    OTP = open(OTPName, 'r').read().split("\n")
    cyphertext = ""
    line = 0
    letterPos = 0
    # for each letter in processed message:
    for letter in plaintext:
        #   - go to corresponding line number and letter number
        padLetter = OTP[line][letterPos]
        # get index of letter on pad
        padIndex = alphabetList.index(padLetter)
        # get plaintext index
        plainIndex = alphabetList.index(letter)
        # calculate index of cipher letter
        cipherIndex = (plainIndex + padIndex) % 26
        #   - encode by adding index of letter
        cyphertext += alphabetList[cipherIndex]

        # calculate next lines index
        line += 1
        letterPos = (letterPos + 1) % 26

    return cyphertext


# decryption:
def decrypt(ciphertext, OTPName):
    global alphabetList
    # read pad as list
    OTP = open(OTPName, 'r').read().split("\n")
    plaintext = ""
    line = 0
    letterPos = 0
    # for each letter in processed message:
    for letter in ciphertext:
        #   - go to corresponding line number
        #   - go to corresponding letter in line
        padLetter = OTP[line][letterPos]
        padIndex = alphabetList.index(padLetter)

        cipherIndex = alphabetList.index(letter)

        #   - decode by substracting index of letter
        plainIndex = (cipherIndex - padIndex + 26) % 26  # to ensure index is positive
        plaintext += alphabetList[plainIndex]
        line += 1
        letterPos = (letterPos+1)%26

    return plaintext


# strip message of spaces and punctuation, make message uppercase
message = raw_input("Enter your message: ")
for char in string.punctuation:
    while char in message:
        message = message.replace(char, "")
message = message.replace(" ", "")
message = message.upper()

encryptedMessage = encrypt(message,'pad.txt')
print "Your encrypted message", encryptedMessage
print "Your decrypted message", decrypt(encryptedMessage, 'pad.txt')