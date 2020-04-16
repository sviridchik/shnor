# import hashlib
# #
# # hash_object = hashlib.sha1(b'1000630')
# # hex_dig = hash_object.hexdigest()
# #
# # print(hex_dig)

# print(hash('1000630'))
import hashlib

hash_object = hashlib.md5(b'1000630')
print(b'1000630')
print(int(hash_object.hexdigest(),16))
# +animation