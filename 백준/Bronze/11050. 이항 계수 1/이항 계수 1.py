def fac(val):
    result = 1
    for i in range(1, val+1):
        result *= i
    return result
N, K = map(int,input().split())
print(fac(N)//(fac(K)*fac(N-K)))