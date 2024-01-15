# O(루트n)의 시간복잡도로 소수구하기
# 1. 만약 양의 정수 N이 소수가 아니라면, N = a*b를 만족하는 두개의 정수 a,b(1<a,b<N)이 존재한다.
# 2. 1-N의 범위에서 a,b 둘중하나가 루트N 보다 크다면 나머지는 루트N 보다 작아야한다.(N = a*b이기 때문에)
# 3. 2~루트N 까지의 수 중에서 N을 나누어 떨어뜨리는 값이 없다면 소수라고 확정할 수 있다.
# ! 소수구할 때 짝수일때까지 한번에 정리하면 시간복잡도를 또 반으로 줄일 수 있다.
import sys, math

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    if num < 2:
        return False
    for i in range(3,int(math.sqrt(num)+1),2):
        if num % i == 0:
            return False
        i += 1
    return True

N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1