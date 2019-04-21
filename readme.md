# Project folder for secure comms labs

'cipher1.py' is lab5. In this lab I was tasked with creating a cipher program that read in a string or int and and gave a number of decoded outputs using rot5, rot13, caesar, or rot47. This was achieved be separating the individual characters or digits out and manipulating thm accordingly and rejoining them before returning them as the result

hasher1.py is lab8. In this lab I was tasked with figuring out how to a authenticate as a user for a given challenge hash using information provided to ve in the question. Basically, I needed to find the hash that hashes to the hash provided in the question. This involved using the seed hash provided and creating a loop that generates and outputs hashes based on the previous hash until the target hash is found. The penultimate hash is the solution.

CreditCard1.py is lab9. This lab tasked me with writing a program that would verify that a user entered credit card number was valid and what vendor issued the card. It would also generate the checksum for a card given the first portion of the card and given a user specified vendor name, generate a valid card number using a checksum.

The completed RSA labs are named with their number. These involved decoding messages using limited information provided in the question.
