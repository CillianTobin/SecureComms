import sys

def rot5_cipher(input):

    digits = [int(i) for i in input]
    for i in range(len(digits)):
            digits[i] = (digits[i] - 5) % 10

    newword = ''.join(str(x) for x in digits)
    #print(digits)
    print(newword)


def rot13_cipher(word):
    letters = list(word)
    for i in range(len(letters)):
        if letters[i].isupper():
            letters[i] = ord(letters[i]) - 65
            letters[i] = (letters[i] + 13) % 26
            letters[i] = letters[i] + 65
            letters[i] = chr(letters[i])
        if letters[i].islower():
            letters[i] = ord(letters[i]) - 97
            letters[i] = (letters[i] + 13) % 26
            letters[i] = letters[i] + 97
            letters[i] = chr(letters[i])
    newword = ''.join(letters)


    print(newword)

def rot47_cipher(string1):
    result = []
    for i in range(len(string1)):
        digit = ord(string1[i])
        if digit >= 33 and digit <= 126:
            result.append(chr(33 + ((digit + 14) % 94)))
        else:
            result.append(string1[i])
    newword = ''.join(result)
    print(newword)


if sys.argv[1].isdigit()==True:
    rot5_cipher(sys.argv[1])
rot13_cipher(sys.argv[1])
rot47_cipher(sys.argv[1])
