import sys

def isPrime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    n = int(input())
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1