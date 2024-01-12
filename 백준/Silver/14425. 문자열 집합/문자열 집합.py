import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sett = set()
result = 0
for i in range(N):
    sett.add(input())
for i in range(M):
    if input() in sett:
        result += 1
print(result)