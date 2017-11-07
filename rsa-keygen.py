#!/usr/bin/env python3
import binascii, pip, sys, argparse, random


#Parses Arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Process flags for the program.')
    parser.add_argument('-p','--public', required= 'True', help='public key file')
    parser.add_argument('-s','--secret', required= 'True', help='secret key file')
    parser.add_argument('-n','--number', required= 'True', help='number of bits')
    results = parser.parse_args(args)
return (results.public, results.secret, results.number)

def multinv(order, value):
    x, y = 0, 1
    a, b = order, value

    while b != 0:
        a, b, c = b, a % b, a // b
        x, y = y - c * x, x
        rv = (1 - y * order) // value
    if rv < 0:
        rv += order

    return rv

def rsa_keygen(num_bits):
    prime1 = randprime(num_bits)
    prime2 = randprime(num_bits)
    N = prime1 * prime2
    order = (prime - 1) * (prime2 - 1)
    e = 7
    d = multinv(order, e)
    return [N, e, d]


p, s, n = check_arg(sys.argv[1:])

public_key = open(p, 'r').read()#Does this need to be 'rb' instead of 'r'?

private_key = open(s, 'rb').read()
