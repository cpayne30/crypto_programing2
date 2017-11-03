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


#def rsa_keygen():


p, s, n = check_arg(sys.argv[1:])

public_key = open(p, 'r').read()#Does this need to be 'rb' instead of 'r'?

private_key = open(s, 'rb').read()
