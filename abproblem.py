#! /usr/bin/python3
import sys

input()
A = input().split(" ")
result = 0

for i in range(len(A)):
    for j in range(i+1, len(A)):
        for k in range(j+1, len(A)):
           # print(i,j,k, end="")
           
            if int(A[i]) + int(A[j]) == int(A[k]):
                result+=1
           #     print("true", end="")
           # print()

print(result)
