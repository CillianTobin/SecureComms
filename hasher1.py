import hashlib

# swaps the cases
some_string = "ECSC"
digits = list(some_string)
for i in range(len(digits)):
    digits[i] = digits[i].swapcase()
new_string = ''.join(digits)

target = 'c89aa2ffb9edcc6604005196b5f0e0e4'

# generates hashes until target - last output is answer
result = new_string
while result != target:
    hash1 = result
    hash1 = hashlib.md5()
    hash1.update(result.encode('utf-8'))
    result = hash1.hexdigest()
    print(result)


