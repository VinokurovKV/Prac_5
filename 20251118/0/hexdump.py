import sys
import binascii

with open(sys.argv[1], 'rb') as file:
    s = file.read()

res = binascii.hexlify(s, b" ", 16)
print(res)
