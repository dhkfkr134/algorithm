# 1. 비교대상 x,y w-x h-y
# 2. 가장 작은거 출력
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, w-x, h-y))