import sys
input = sys.stdin.readline
n = int(input())
isprime = [1]*1000001
isprime[1] = 0
isprime[0] = 0
# 에라토스테네스의 체
for i in range(2,int(1000001**0.5)+1):
    if isprime[i]:
        for j in range(i*2,1000001,i):
            isprime[j] = 0

# 이것도 투포인터인가? 아무튼 (n/2*100) = 50,000,000번실행
for _ in range(n):
    m = int(input())
    count = 0
    for j in range(1,m//2+1):
        if isprime[j] and isprime[m-j]:
            count += 1
    print(count)
