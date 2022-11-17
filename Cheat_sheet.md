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

[Basic And Extended]https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

> We say that two integers are congruent modulo m if `a ≡ b mod m`. Another way of saying this, is that when we divide the integer `a` by `m`, the remainder is `b`. This tells you that if `m` divides `a` (this can be written as `m | a`) then `a ≡ 0 mod m`.

> Fermat’s little theorem states that if `p` is a prime number, then for any integer `a`, the number `a^p – a` is an integer multiple of `p`.
```
Here p is a prime number

a^p ≡ a (mod p)
```

https://www.geeksforgeeks.org/fermats-little-theorem/

> We say that an integer `x` is a Quadratic Residue if there exists an a such that `a^2 = x mod p`. If there is no such solution, then the integer is a Quadratic Non-Residue.
