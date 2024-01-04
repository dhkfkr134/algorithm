# 가장작은 x1, 가장큰 x2, 가장작은 y1, 가장큰 y2를 찾자
# (x2 - x1) * (y2 - y1) 가 결과
# 좌표가 -10000 ~ 10000 이므로 고려하기

import sys
n = int(input())
X = []
Y = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

print((X[len(X)-1] - X[0])*(Y[len(X)-1] - Y[0]))