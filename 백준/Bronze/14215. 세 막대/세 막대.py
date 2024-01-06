# 삼각형이 될 수 없는 조건일때는 무조건 짧은 두변의 합*2 -1 이다.
import sys
sides = list(map(int, sys.stdin.readline().split()))
sides.sort()
if sides[2] >= sides[1] + sides[0]:
    print((sides[1]+sides[0])*2 - 1)
else:
    print(sum(sides))