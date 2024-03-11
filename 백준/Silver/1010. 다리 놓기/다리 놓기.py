# 조합 정석으로

import sys

def fac(val):
    result = 1
    for i in range(1, val+1):
        result *= i
    return result

input()
lines = sys.stdin.readlines()
for line in lines:
    K, N = map(int,line.split())
    print(fac(N)//(fac(K)*fac(N-K)))