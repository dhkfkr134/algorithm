import sys

input = sys.stdin.readline

N = int(input())
sangeun = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
dic = {sangeun[i]:1 for i in range(N)}

for i in nums:
    if dic.get(i):
        print(1,end=' ')
    else:
        print(0,end=' ')