import sys

def rot5_cipher(input):

    digits = [int(i) for i in input]  # separates digits
    for i in range(len(digits)):  # manipulates digits
            digits[i] = (digits[i] - 5) % 10

    newword = ''.join(str(x) for x in digits)  # rejoins digits
    #print(digits)
    print(newword)


def rot13_cipher(word):
    letters = list(word)  # sepates chars
    for i in range(len(letters)):  # loop through list
        if letters[i].isupper():  # if upper case, for each letter (letter[i]) do these
            letters[i] = ord(letters[i]) - 65
            letters[i] = (letters[i] + 13) % 26
            letters[i] = letters[i] + 65
            letters[i] = chr(letters[i])
        if letters[i].islower():  # if lower case, for each letter (letter[i]) do these
            letters[i] = ord(letters[i]) - 97
            letters[i] = (letters[i] + 13) % 26
            letters[i] = letters[i] + 97
            letters[i] = chr(letters[i])
    newword = ''.join(letters)  # rejoin


    print(newword)

def rot47_cipher(string1):
    result = []
    for i in range(len(string1)):
        digit = ord(string1[i])  # return int value(ascii)
        if digit >= 33 and digit <= 126:  # if within ascii do this
            result.append(chr(33 + ((digit + 14) % 94)))  # rotate and append to list
        else:
            result.append(string1[i])  # append to list
    newword = ''.join(result)  # rejoin string
    print(newword)


if sys.argv[1].isdigit()==True:
    rot5_cipher(sys.argv[1])
rot13_cipher(sys.argv[1])
rot47_cipher(sys.argv[1])
