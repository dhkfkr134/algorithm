# 1. 배열에서 순서 그냥 추가해버림
import sys
N = int(input())
arr = list([0, 0, 0] for _ in range(N))
for i in range(N):
    arr[i] = sys.stdin.readline().split()
    arr[i].append(i)
arr.sort(key=lambda x: (int(x[0]), x[2]))
for a in arr:
    print(a[0],a[1])