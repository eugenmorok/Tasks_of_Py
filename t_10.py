print(str.lower.__doc__)

import sys
import hashlib

hash_password = 'c8b667f4e6953d59b6ae9b9659772333'
input_raw_pass = sys.argv[1]
input_encode_pass = input_raw_pass.encode()
input_hash_pass = hashlib.md5(input_encode_pass)
input_hex_pass = input_hash_pass.hexdigest()
if hash_password == input_hex_pass:
    print("Доступ открыт")
else:
    print("Доступ закрыт")
print(hash_password)
print(input_raw_pass)
print(input_encode_pass)
print(input_hash_pass)
print(input_hex_pass)