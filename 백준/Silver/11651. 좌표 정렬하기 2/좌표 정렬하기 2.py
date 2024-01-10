# 파이썬에서 람다식 알아보고 가자
import sys
N = int(input())
arr = list([0, 0] for _ in range(N))
for i in range(N):
    arr[i][0], arr[i][1] = map(int,sys.stdin.readline().split())
arr.sort(key=lambda x: (x[1], x[0]))
for a in arr:
    print(a[0], a[1])