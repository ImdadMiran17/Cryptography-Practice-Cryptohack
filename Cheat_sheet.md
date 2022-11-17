# Cryptography-Practice-Cryptohack

### Introduction

> In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite).

> In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.

> In Python, after importing the base64 module with `import base64`, you can use the `base64.b64encode()` function. Remember to decode the hex first as the challenge description states.

> Python's PyCryptodome library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with `from Crypto.Util.number import *`.

> The Python `pwntools` library has a convenient `xor()` function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.

### Modular Arithmetic

> We say that for any two integers `a,b`, if `gcd(a,b) = 1` then `a` and `b` are coprime integers.If `a` and `b` are prime, they are also coprime. If `a` is prime and `b < a` then `a` and `b` are coprime.

> Let `a` and `b` be positive integers.The extended Euclidean algorithm is an efficient way to find integers `u,v` such that
`a * u + b * v = gcd(a,b)`
https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

>
