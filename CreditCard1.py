import sys


def card_checker(input_value):  # takes in card number checks if valid

    digits = [int(i) for i in input_value]
    print("Original digits          = ", digits)
    last_digit = digits[len(digits) - 1]  # get last digit value
    new_digits = digits[:-1]  # remove last digit
    flipped_digits = new_digits[::-1]
    print("Flipped digits           = ", flipped_digits)
    even_digits = flipped_digits[0::2]
    print("Evens                    = ", even_digits)
    odd_digits = flipped_digits[1::2]
    print("Odds                     = ", odd_digits)

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

    sum_of_luhn1 = 0
    for i in range(len(final_luhn1)):
        sum_of_luhn1 = sum_of_luhn1 + final_luhn1[i]

    print("Even digits after change = ", even_digits)
    print("Odd digits after change  = ", odd_digits)
    print("Final Luhn               = ", final_luhn1)
    print("Sum of Luhned-nums       = ", sum_of_luhn1)
    mod_of_sum = sum_of_luhn1 % 10
    print("Mod of sum               = ", mod_of_sum)
    print("Last Digit               = ", last_digit)

    if sum_of_luhn1 % 10 == last_digit:
            print("!!!THIS IS A VALID CARD!!!")
    else:
            print("Invalid Card...")


def vendor_checker(input_value):

    vendor = ""
    digits = [int(i) for i in input_value]
    # FIGURE OUT HOW TO DO THESE COMPLEX IF STATEMENTS !

    if len(digits) == 15:  # Check for American Express
        vendor = "American Express"
        print("The Vendor is ", vendor)

    if digits[0] == (5, 1):
        if len(digits) == 16:
            print("The Vendor id MasterCard!")

    visa_electron_list = [0o26, 175, 508, 844, 913, 917]
    if digits[0] == 4:
        if digits[1:3] in visa_electron_list:
            print("The Vendor is Visa Electron!")
        else:
            print("The Vendor is Visa!")

    if digits[0:1] == (3, 6):
        print("The Vendor is Diners Club - International!")

def card_generator(input_value):



print(card_checker(sys.argv[1]))
print(vendor_checker(sys.argv[1]))

