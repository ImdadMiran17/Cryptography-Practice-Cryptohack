import binascii
from pwn import *

encoded = binascii.unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
hint = "crypto{}"
hint_byte = hint.encode()
hintt = xor(encoded, hint_byte)
print(hintt)

key = "myXORkey"
key_byte = key.encode()

flag = xor(encoded, key_byte)
print(flag)
