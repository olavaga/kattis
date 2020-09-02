!# /usr/bin/python3

def lettertonumber(letter):
    conversion = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    return conversion[letter]

def numbertoletter(number):
    conversion = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
    return conversion[number]

def possiblemove(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    xdiff = lettertonumber(x2) - lettertonumber(x1)
    ydiff = y2 - y1

    if abs(xdiff) == abs(ydiff):
        return True
    else:
        return False

