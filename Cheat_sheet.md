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

[Basic And Extended](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/)

> We say that two integers are congruent modulo m if `a ≡ b mod m`. Another way of saying this, is that when we divide the integer `a` by `m`, the remainder is `b`. This tells you that if `m` divides `a` (this can be written as `m | a`) then `a ≡ 0 mod m`.

> Fermat’s little theorem states that if `p` is a prime number, then for any integer `a`, the number `a^p – a` is an integer multiple of `p`.
```
Here p is a prime number
a^p ≡ a (mod p)
```

[Fermats Little Theorem](https://www.geeksforgeeks.org/fermats-little-theorem/)

> We say that an integer `x` is a Quadratic Residue if there exists an a such that `a^2 = x mod p`. If there is no such solution, then the integer is a Quadratic Non-Residue. In other words, `x` is a quadratic residue when it is possible to take the square root of `x` modulo an integer `p`.

```
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue
```

> The Legendre Symbol gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime p.
> Legendre's Symbol: `(a / p) ≡ a^(p-1)/2 mod p` obeys:
```
(a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
(a / p) = -1 if a is a quadratic non-residue mod p
(a / p) = 0 if a ≡ 0 mod p
```
Which means given any integer `a`, calculating `pow(a,(p-1)/2,p)` is enough to determine if a is a quadratic residue.

> All primes that aren't 2 are of the form `p ≡ 1 mod 4` or `p ≡ 3 mod 4`, since all odd numbers obey these congruences. In the `p ≡ 3 mod 4` case, a really simple formula for computing square roots can be derived directly from Fermat's little theorem. That leaves us still with the `p ≡ 1 mod 4` case, so a more general algorithm is required. In a congruence of the form `r^2 ≡ a mod p`, Tonelli-Shanks calculates `r`.

> Tonelli-Shanks doesn't work for composite (non-prime) moduli. Finding square roots modulo composites is computationally equivalent to integer factorization.

[Tonelli Shanks](https://www.geeksforgeeks.org/find-square-root-modulo-p-set-2-shanks-tonelli-algorithm/)

> The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime. This means, that given a set of arbitrary integers a<sub>i</sub>, and pairwise coprime integers n<sub>i</sub>, such that the following linear congruences hold:
```
x ≡ a1 mod n1
x ≡ a2 mod n2
...
x ≡ an mod nn
```
There is a unique solution `x ≡ a mod N` where `N = n1 * n2 * ... * nn`.

> "Pairwise coprime integers" means that if we have a set of integers `{n1, n2, ..., ni}`, all pairs of integers selected from the set are coprime: `gcd(ni, nj) = 1`.

[Chinese Remainder Theorem](https://www.geeksforgeeks.org/chinese-remainder-theorem-set-1-introduction/)



