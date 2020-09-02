#! /usr/bin/python3
import sys

for formula in sys.stdin:
    symbols = {'CAKE':[], 'N':[], 'pqrst':[]}

    if '0' in formula:
        continue

    for letter in formula:
        for key in symbols:
            if letter in key:
                symbols[key].append(letter)
                break

    if symbols['pqrst']:
        res = symbols['pqrst'].pop()

        while symbols['CAKE'] and symbols['pqrst']:
            res = symbols['CAKE'].pop() + symbols['pqrst'].pop() + res

        for n in symbols['N']:
            res = 'N' + res

        print(res)

    else:
        print("no WFF possible")
    
