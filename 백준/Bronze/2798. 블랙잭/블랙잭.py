# N이 100까지니깐 O(n^3)로 풀어도 100*99*98/6 = 161700 < 10^6

import sys, math
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for k in range(N):
    for i in range(k+1, N):
        for j in range(i+1, N):
            if arr[k] + arr[i] + arr[j] <= M:
                result = max(arr[k] + arr[i] + arr[j], result)
print(result)