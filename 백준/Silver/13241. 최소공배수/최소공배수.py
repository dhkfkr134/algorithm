# 유클리드 호제법
# 1. 최소 공배수 : 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.
# 2. 최대 공약수 : 2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
import sys
input = sys.stdin.readline

A,B = map(int,input().split())
MA, MB = A, B
while MB != 0:
    MA = MA % MB
    MA, MB = MB, MA
print(A*B//MA)
