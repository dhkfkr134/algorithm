# 1. 뭔가 간단한 방법이 생각 안남
# 2. x와 y를 따로 비교한다.
# 3. x값중 한개만 있으면 그 값이 찾으려는 점의 x, y도 마찬가지
import sys
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(3))
tempx = arr[0][0]
tempy = arr[0][1]
cntx = 0
cnty = 0
x = 0
y = 0
for i in range(2):
    if tempx != arr[i+1][0]:
        x = arr[i+1][0]
        cntx += 1
        if cntx == 2:
            x = tempx
    if tempy != arr[i+1][1]:
        y = arr[i+1][1]
        cnty += 1
        if cnty == 2:
            y = tempy

print(f'{x} {y}')
