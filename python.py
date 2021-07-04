import hashlib
mystring = input('Enter String to hash: ')
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())
