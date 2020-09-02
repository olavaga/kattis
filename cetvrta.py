#! /usr/bin/python3
import sys

seen_x, seen_y = {}, {}
n_read = 0

for point in sys.stdin:
    x_in, y_in = point.split()

    if x_in in seen_x:
        seen_x[x_in] += 1
    else:
        seen_x[x_in] = 1
        
    if y_in in seen_y:
        seen_y[y_in] += 1
    else:
        seen_y[y_in] = 1
    
    n_read += 1
    if n_read == 3:
        break

final_x, final_y = -1, -1

for x in seen_x:
    if seen_x[x] == 1:
        final_x = x

for y in seen_y:
    if seen_y[y] == 1:
        final_y = y
        
print(final_x, final_y)


