# Name: Vivian Feng and Shriya Muthukumar
# Date: March 6, 2020

# Vignere.py
import string


# helper functions
# letter to index
def letterToIndex(ch):
    alphabet = string.ascii_uppercase
    idx = alphabet.find(ch)
    if idx < 0:
        print "error: letter not in the alphabet", ch
    return idx

# index to letter
def indexToLetter(idx):
    alphabet = string.ascii_uppercase
    if idx > 25:
        print "error: ", idx, 'is too large'
        letter = ""
    elif idx < 0:
        print " error: ", idx, " is less than 0"
        letter = ""
    else:
        letter = alphabet[idx]
    return letter


# looking up a letter in the Vignere square
def vignereIndex(keyLetter, plainTextLetter):
    keyIndex = letterToIndex(keyLetter)
    ptIndex = letterToIndex(plainTextLetter)
    newIdx = (ptIndex+keyIndex)%26
    return indexToLetter(newIdx)

def vignereIndexRev(keyLetter, cypherLetter):
    #ind row of table corresponding to key
    # find position of ciphertext letter in that row
    # use the columns label as plaintext
    keyIndex = letterToIndex(keyLetter)
    cypherIndex = letterToIndex(cypherLetter)
    newIdx = (cypherIndex-keyIndex)%26
    return indexToLetter(newIdx)

# encrypting a message using the Vignere cipher
def encryptVignere(key, plainText):
    cipherText = ""
    keyLen = len(key)
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == ' ':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + vignereIndex(key[i % keyLen], ch)

    return cipherText


# decrypt a message
def decryptVignere(key, encypheredText):
    plainText = ""
    keyLen = len(key)
    for i in range(len(encypheredText)):
        ch = encypheredText[i]
        if ch == ' ':
            plainText = plainText + ch
        else:
            plainText = plainText + vignereIndexRev(key[i % keyLen], ch)

    return plainText
#
# messageOne = "THE EAGLE HAS LANDED"
# keyOne = "DAVINCI"
#
# enStr = decryptVignere(keyOne,encryptVignere(keyOne, messageOne))
# print enStr

print decryptVignere("DAVINCI","QO WEFQQAMG LWHS")
