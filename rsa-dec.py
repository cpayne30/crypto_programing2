#!/usr/bin/env python3
import binascii, pip, sys, argparse, random


#Parses Arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Process flags for the program.')
    parser.add_argument('-k','--key', required= 'True', help='key file')
    parser.add_argument('-i','--input', required= 'True', help='input file')
    parser.add_argument('-o','--output', required= 'True', help='output file')
    results = parser.parse_args(args)
return (results.key, results.input, results.output)


#def rsa_decrypt():


k, i, o = check_arg(sys.argv[1:])

key = open(k, 'r').read()

in_string = open(i, 'rb').read()
output = open(o, 'wb')
