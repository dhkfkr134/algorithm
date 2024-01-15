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

def solve():
    N = int(sys.stdin.readline())
    for _ in range(N):
        n = int(sys.stdin.readline())
        while True:
            if isPrime(n):
                print(n)
                break
            else:
                n += 1
solve()
