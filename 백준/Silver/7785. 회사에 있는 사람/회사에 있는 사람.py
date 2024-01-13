# 1. 중복제거 -> 같은 사람이 두번 들어 있으면 나중것만 남게됨 -> 그러면 person : leave가 된다.
# 2. 입력을 리스트로도 받아둔다. 중복을 제거한다.
# 3. 내림차순으로 정렬하고 마지막결과가 enter인 사람만 출력한다.
import sys
input = sys.stdin.readline
N = int(input())
arr = []
dic = {}
for i in range(N):
    x, y = map(str, input().split())
    dic[x] = y
    arr.append(x)

arr = sorted(list(dic), reverse=True)

for key in arr:
    if dic[key] == 'enter':
        print(key)