import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic ={}
result = 0
for i in range(N):
    dic[input()] = 1
for i in range(M):
    if dic.get(input()):
        result += 1
print(result)