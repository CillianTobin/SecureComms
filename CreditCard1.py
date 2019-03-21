import sys
import random


def card_checker(input_value):  # takes in card number checks if valid

    digits = [int(i) for i in input_value]
    last_digit = digits[len(digits) - 1]  # get last digit value
    new_digits = digits[:-1]  # remove last digit
    flipped_digits = new_digits[::-1]
    even_digits = flipped_digits[0::2]
    odd_digits = flipped_digits[1::2]

    for i in range(len(even_digits)):  # multiply nums in list by 2
        even_digits[i] = even_digits[i] * 2
        if even_digits[i] > 9:  # if more than 9...
            even_digits[i] = even_digits[i] - 9

    final_luhn1 = []
    for i in range(len(odd_digits)):  # re-concatenate digits by weaving in evens and odds to new list
        final_luhn1.append(even_digits[i])
        final_luhn1.append(odd_digits[i])
# loop misses last even digit because list lengths are different after final digit is removed from even card number
    if len(digits) % 2 == 0:
        final_luhn1.append(even_digits[len(even_digits) - 1])  # adds in final evenDigit if original card no. is even
    
    final_sum1 = 0
    for i in range(len(final_luhn1)):
        final_sum1 = final_sum1 + final_luhn1[i]
    final_sum1 = final_sum1 + last_digit
    mod_of_sum = final_sum1 % 10

    if mod_of_sum == 0:
            return "!!!THIS IS A VALID CARD!!!"
    else:
            return "Invalid Card..."


def vendor_checker(input_value):
    digits = [int(i) for i in input_value]

# AMERICAN EXPRESS
    if len(digits) == 15:  # Check for American Express
        return "The Vendor is American Express"

# MASTERCARD/MAESTRO
    if digits[0] == 5:
        if digits[1] > 0 and digits[1] < 6:
            return "The Vendor is MasterCard!"
        else:
            return "The Vendor is Maestro!"
    first_six = ''.join(str(x) for x in digits[:6])
    if int(first_six) >= 222100 and int(first_six) <= 272099:
        return "The Vendor is Mastercard!"

# DISCOVERY/INSTAPAYMENT/rest of MAESTRO
    if digits[0] == 6:
        # next 5 check for maestro
        dcheck1 = [6, 3, 0, 4]
        if digits[:4] == dcheck1[:4]:
            return "The Vendor is Maestro!"
        dcheck2 = [6, 7, 5, 9]
        if digits[:4] == dcheck2[:4]:
            return "The Vendor is Maestro!"
        dcheck3 = [6, 7, 6, 1]
        if digits[:4] == dcheck3[:4]:
            return "The Vendor is Maestro!"
        dcheck4 = [6, 7, 6, 2]
        if digits[:4] == dcheck4[:4]:
            return "The Vendor is Maestro!"
        dcheck5 = [6, 7, 6, 3]
        if digits[:4] == dcheck5[:4]:
            return "The Vendor is Maestro!"
        # check for instapayment

        if digits[1] == 3:
            if digits[2] >=7 and digits[2] <= 9:
                return "The Vendor is InstaPayment!"
        # everything else beginning with 6 is discovery
        else:
            return "The Vendor is Discovery!"

# VISA
    if digits[0] == 4:
        vcheck1 = [4, 0, 2, 6]
        if digits[:4] == vcheck1[:4]:
            return "The Vendor is Visa Electron!"
        vcheck2 = [4, 1, 7, 6]
        if digits[:4] == vcheck2[:4]:
            return "The Vendor is Visa Electron!"
        vcheck3 = [4, 5, 0, 8]
        if digits[:4] == vcheck3[:4]:
            return "The Vendor is Visa Electron!"
        vcheck4 = [4, 8, 4, 4]
        if digits[:4] == vcheck4[:4]:
            return "The Vendor is Visa Electron!"
        vcheck5 = [4, 9, 1, 3]
        if digits[:4] == vcheck5[:4]:
            return "The Vendor is Visa Electron!"
        vcheck6 = [4, 9, 1, 7]
        if digits[:4] == vcheck6[:4]:
            return "The Vendor is Visa Electron!"
        else:
            return "The Vendor is Visa!"

# DINERS CLUB
    if digits[0] == 3:
        if len(digits) == 14:
            if digits[1] == 6:
                return "The Vendor is Diners Club - International!"
            else:
                return "The Vendor is Diners Club - Carte Blanche!"
        first_four = ''.join(str(x) for x in digits[:4])
        if int(first_four) >= 3528 and int(first_four) <= 3589:
            return "The Vendor is JCB!"
# ANY NOT CAUGHT
    else:
        return "The exact card vendor was not identified"


def calculate_checksum(input_value):
    digits = [int(i) for i in input_value]
    last_digit = digits[len(digits) - 1]  # get last digit value
    new_digits = digits[:-1]  # remove last digit
    flipped_digits = new_digits[::-1]
    even_digits = flipped_digits[0::2]
    odd_digits = flipped_digits[1::2]

    for i in range(len(even_digits)):  # multiply nums in list by 2
        even_digits[i] = even_digits[i] * 2
        if even_digits[i] > 9:  # if more than 9...
            even_digits[i] = even_digits[i] - 9

    final_luhn1 = []
    for i in range(len(odd_digits)):  # re-concatenate digits by weaving in evens and odds to new list
        final_luhn1.append(even_digits[i])
        final_luhn1.append(odd_digits[i])
        # loop misses last even because list lengths are different after final digit is removed from even card number
    if len(digits) % 2 == 0:
        final_luhn1.append(even_digits[len(even_digits) - 1])  # adds in final evenDigit if original card no. is even

    final_sum2 = 0
    for i in range(len(final_luhn1)):
        final_sum2 = final_sum2 + final_luhn1[i]
    final_sum2 = final_sum2 + last_digit

    mod_of_sum = final_sum2 % 10  # These lines calculates checksum
    #print(mod_of_sum)
    checker = 0
    checksum = 0
    if mod_of_sum > 0:
        checksum = 10 - mod_of_sum
        checker = mod_of_sum + checksum
    final = checker % 10  # this should be 0 i valid
    #print("if valid this should be zero =>", final)
    print("The checksum for this first portion of a number is", checksum)


def generate_card_number(input_value):

    factors = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

    while True:
        digits = [random.randint(0, 9) for i in range(0, 16)]

# handle specific vendor parameters

        if input_value == "visa":
            digits[0] = 4
        if input_value == "visa-electron":
            digits[:4] = [4, 0, 2, 3]
        if input_value == "discover":
            digits[0] = 6
            digits[1] = 2
        if input_value == "mastercard":
            i = random.choice([5, 1, 6, 2, 7])  # random number from list, accounts for luhn x2 to make 1-5
            digits[:2] = [5, i]
        if input_value == "maestro":
            i = random.choice([0, 4])
            digits[:2] = [5, i]
        if input_value == "instapayment":
            i = random.randint(7, 9)
            digits[:3] = [6, 6, i]  # accounts for luhn x2 this should make 3, 6, 7-9 ???
        if input_value == "american express":
            digits = digits[:-1]
            i = random.choice([2, 8])
            digits[:2] = [3, i]
        if input_value == "jcb":
            i = random.choice([1, 6, 2, 7, 3, 8, 4])
            digits[:4] = [3, 5, i]
        if input_value == "diners-club":
            i = random.choice([0, 5, 1, 6, 2, 7])
            digits[:3] = [3, 0, i]

# take vendor specific number and make sure its valid before returning it
# new card checker method, wish i just did this for card_checker :(

        last_digit = digits[len(digits) - 1]  # get last digit value
        digits = digits[:-1]  # remove last digit
        digits = digits[::-1]  # reverse digits

        luhned = []
        for x in range(len(digits)):  # used different(better) method to do luhn check( don't need evens and odds)
            digits[x] = digits[x] * factors[x]  # just multiply by a list looping along side it
            if digits[x] > 9:
                digits[x] = digits[x] - 9
            luhned.append(digits[x])  # rejoin

        final_sum1 = 0
        digits = digits[::-1]
        for i in range(len(luhned)):
            final_sum1 = final_sum1 + luhned[i]
        final_sum1 = final_sum1 + last_digit
        mod_of_sum = final_sum1 % 10
        if mod_of_sum == 0:  # final validation check
            digits.append(last_digit)
            joined = ''.join(str(x) for x in digits)
            print("Valid", input_value, "card number:")
            return joined
        # if not valid while loop will continue until one is found.


# call functions
s = sys.argv[1]
if s.isdigit():
    print(card_checker(s))
    print(vendor_checker(s))
    calculate_checksum(s)
if s.isalpha():
    print(generate_card_number(s))
