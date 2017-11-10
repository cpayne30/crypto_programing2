#!/usr/bin/env python3
import binascii, pip, sys, argparse, random

def ProbPrimeRabinMiller(n):
  """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.
    """
  small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
  k = 4
  if n < 2: return False
  for p in small_primes:
    if n < p * p: return True
    if n % p == 0: return False
  r, s = 0, n - 1
  while s % 2 == 0:
    r += 1
    s //= 2
  for _ in range(k):
    a = random.randrange(2, n - 1)
    x = pow(a, s, n)
    if x == 1 or x == n - 1:
      continue
    for _ in range(r - 1):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True

def prime_gen(bit_len):
  while True:
    prime = random.getrandbits(bit_len)
    prime = prime | bit_len

    if ProbPrimeRabinMiller(prime): break

  return prime

for i in range (0, 100):
  rv = prime_gen(24)
  print (bin(rv), rv)
