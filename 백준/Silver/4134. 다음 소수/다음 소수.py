# O(루트n)의 시간복잡도로 소수구하기
# 1. 만약 양의 정수 N이 소수가 아니라면, N = a*b를 만족하는 두개의 정수 a,b(1<a,b<N)이 존재한다.
# 2. 1-N의 범위에서 a,b 둘중하나가 루트N 보다 크다면 나머지는 루트N 보다 작아야한다.(N = a*b이기 때문에)
# 3. 2~루트N 까지의 수 중에서 N을 나누어 떨어뜨리는 값이 없다면 소수라고 확정할 수 있다.
import sys, math

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
# 결이 같은 코드같은데 왜 시간차이가 나지?
# input = sys.stdin.readline
# N = int(input())
# # 입력값 N개
# for _ in range(N):
#     # 소수찾을 기준 값
#     n = int(input())
#     # n위로 소수찾을때까지 돌림
#     while True:
#         isSosu = False
#         i = 2
#         # i*i = n인 i는 루트n, 즉 루트n까지 탐색
#         if n>3:
#             while i*i <= n:
#                 # 나누어 떨어지면 합성수이기때문에 n+1숫자로 넘어가서 탐색
#                 if n % i == 0:
#                     isSosu = False
#                     break
#                 # 끝까지 안나눠지면 소수
#                 else:
#                     isSosu = True
#                     i+=1
#             if isSosu:
#                 print(n)
#                 break
#             n += 1
# 
#         elif n==3:
#             print(3)
#             break
#         else:
#             print(2)
#             break