from Crypto.PublicKey import RSA

key = RSA.importKey(open('RSA/mykey2.pem', 'r').read())  # read in file, use the crypto stuff

print("key n is ", key.n)  # print out key.n which is found for you using above line
print("key e is ", key.e)
print("key d is ", key.d)

print('ZD{', key.n, ",", key.e, ",", key.d, "}")  # remove spaces for copy/paste




