# 유클리드 호제법
# 1. 최소 공배수 : 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.
# 2. 최대 공약수 : 2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
import sys
input = sys.stdin.readline

A,B = map(int,input().split())
C,D = map(int,input().split())
MB, MD = B, D
while MD != 0:
    MB = MB % MD
    MB, MD = MD, MB
mom = B*D//MB
child = (mom//B)*A+C*(mom//D)
mm, mc = child, mom
while mc != 0:
    mm = mm % mc
    mm, mc = mc, mm
print(child//mm,mom//mm)