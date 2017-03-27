import string

def alphabet_position(char):
    index=0
    lalphabet = 'abcdefghijklmnopqrstuvwxyz'
    ualphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if char in lalphabet:
        index = lalphabet.find(char)
        return index
    if char in ualphabet:
        index = ualphabet.find(char)
        return index


    if char not in lalphabet or ualphabet:
        return char

def rotate_char(char, rot):
    lalphabet = 'abcdefghijklmnopqrstuvwxyz'
    ualphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.isdigit():
        return char
    if char in string.punctuation:
        return char
    if char == " ":
        return char
    hld = char
    char = alphabet_position(char)
    move = (char + rot) % 26
    if hld in lalphabet:
        return lalphabet[move]
    if hld in ualphabet:
        return ualphabet[move]

def encrypt(text, rot):
    encrypted = ""

    for char in text:
        encrypted = encrypted + rotate_char(char, rot)

    return encrypted
