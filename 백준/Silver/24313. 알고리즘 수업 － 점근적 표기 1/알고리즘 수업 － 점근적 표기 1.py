# 그냥 문제 그대로 짜봄
# f(n)의 기울기는 음수일 수 있는거 확인

a, b = map(int, input().split())
c = int(input())
n0 = int(input())

def funcf(n):
    return a*n + b

def funcg(n):
    return n

if funcf(n0) <= c*funcg(n0) and a <= c:
    print(1)
else:
    print(0)