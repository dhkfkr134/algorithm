# 1. 유클리드 호제법 - 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.
import sys
input = sys.stdin.readline

N = int(input())
M = 0
for i in range(N):
    A, B = map(int, input().split())
    for j in range(min(A,B),0,-1):
        if A % j == 0 and B % j ==0:
            M = j
            break
    print(A*B//M)