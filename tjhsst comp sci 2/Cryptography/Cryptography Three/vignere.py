#Name: Shriya Muthukumar and Vivan Feng
#Date: 3/6/2020

#encrypt using vignere cipher

#helper functions
#letter to index
def letterToIndex(ch):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    idx = alphabet.find(ch)
    if idx < 0:
        print("error: letter not in the alphabet", ch)
    return idx

#index to letter
def indexToLetter(idx):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    if idx > 25:
        print('error: ', idx, 'is too large')
        letter = ''
    elif idx < 0:
        print ('error: ', idx, 'is less than 0')
        letter = ''
    else:
        letter = alphabet[idx]
    return letter

#looking up a letter in the Vignere square
def vignereIndex(keyLetter, plainTextLetter):
    keyIndex = letterToIndex(keyLetter)
    ptIndex = letterToIndex(plainTextLetter)
    newIdx = (ptIndex + keyIndex)%26
    return indexToLetter(newIdx)


#encrypting a message using the Vignere cipher
def encryptVignere(key, plainText):
    cipherText = ""
    keyLen = len(key)
    for i in range (len(plainText)):
        ch = plainText[i]
        if ch == ' ':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + vignereIndex(key[i%keyLen], ch)
    return cipherText

def undoVig(keyLetter, ctLetter):
    
    sub1 = letterToIndex(keyLetter)
    sub2 = letterToIndex(ctLetter)
    sub3 = sub2 - sub1
    if sub3 < 0:
        sub3 = (sub2 - sub1) + 26
    return indexToLetter(sub3)

#takes the keyword and returns the plaintext 
def decryptVignere(key, cipherText):
    plainText = ""
    keyLen = len(key)
    for i in range (len(cipherText)):
        ch = cipherText[i]
        if ch == ' ':
            plainText = plainText + ch
        else:
            plainText = plainText + undoVig(key[i%keyLen], ch)
    return plainText


messageOne = "QO WEFQQAMG LWHS"
keyOne = "DAVINCI"

repeatKey = decryptVignere(keyOne, messageOne)

print repeatKey