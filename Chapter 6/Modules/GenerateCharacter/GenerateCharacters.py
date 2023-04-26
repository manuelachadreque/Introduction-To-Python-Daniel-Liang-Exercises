from random import randint

#Generate random between ch1 and ch2

def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1),ord(ch2)))

#Generate random lowercase
def generateLowerCase():
    return getRandomCharacter('a', 'z')

def getUpperCase():
    return getRandomCharacter('A', 'Z')
# Generate random digit character

def getRandomDigit():
    return getRandomCharacter('0','9')

#Generate random character

def getRandmomASCIICharacter():
    return getRandomCharacter(0,127)

