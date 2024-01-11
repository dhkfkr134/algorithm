# 1. 길이에 따라 오름차순
# 2. 문자열에 따라 오름차순
#    중복된 단어는 한개만 출력
import sys
N = int(input())
arr = list([0, 0] for _ in range(N))
for i in range(N):
    arr[i][0] = input()
    arr[i][1] = len(arr[i][0])
arr.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    if i > 0 and arr[i-1][0] != arr[i][0]:
        print(arr[i][0])
    elif i == 0:
        print(arr[0][0])