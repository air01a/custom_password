#!/usr/bin/python3

import argparse


def password_generator(word, worlist, prefix=''):
    for x in range(0, 2**len(word)):
        for i in range(0, len(word)):
            if 2**i & x == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
        wordlist.write(prefix+word + "\n")
        for i in range(0, 99):
            wordlist.write(prefix + word + str(i) + "\n")
        for i in range(2005, 2016):
            wordlist.write(prefix + word + str(i) + "\n")

parser = argparse.ArgumentParser(prog='pass.py',
                                 usage='%(prog)s words [OPTIONS]',
                                 description='Create custom passwords list.\
                                 Capitalize some letters:\
                                 dog => Dog, DOg, DOG,dOg etc.\
                                 Add number from 0 to 99 and from 1950 to 2016\
                                 at the end of the passwords')
parser.add_argument('words', nargs='*',
                    action='append',
                    help='List of known words, separated by space.')
parser.add_argument('-o', '--output',
                    dest='output',
                    default='wordlist.txt',
                    help='Name of the output file. (Default: wordlist.txt)')
parser.add_argument('-p', '--prefix',
                    dest='prefix',
                    default='',
                    help='Prefix every password generated with one word')
args = parser.parse_args()


try:
    wordlist = open(args.output, 'w')
except IOError:
    print('Cannot open', args.output)
else:
    for word in args.words[0]:
        password_generator(word, wordlist, args.prefix)

    wordlist.close()
