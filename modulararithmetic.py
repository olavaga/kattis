#!usr/bin/python3
import sys

t = 0

for line in sys.stdin:
	#print("Evaluating line:", line)

	if t == 0:
		#print("t is zero")
		n, t = line.split()
		n, t = int(n), int(t)
		#print("assigned t", t, "and n",n)
		continue

	#if t == 0 and n == 0:
		#print("exiting")
	#	break

	#print("Splitting line")
	x, op, y = line.split()
	x, y = int(x), int(y)
	result = -1
	if (op == "+"):
		result = (x + y) % n

	if (op == "-"):
		result = (x - y) % n

	if (op == "*"):
		result = (x * y) % n

	if (op == "/" and y != 0):
		result =  (x * (y**(-1))) % n

	print(result)
	t -= 1
	#print("T is now", t)
		
