#!/usr/bin/python3

for letter in range(122, 96, -2):
    print("{:c}{:c}".format(letter, letter - 33), end='')
