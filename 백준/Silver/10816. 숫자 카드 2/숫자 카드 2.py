# 1. 내가 아직 많이 부족한게 분명 Counter를 배웠는데 생각이 잘 안났다.
# 2. 배열에서 값 하나하나 비교하면서 dictionary값을 ++할 생각으로 짜다가 생각이 났다.
# 3. 파이썬은 다 알고만 있으면 참 편리하다
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
sangguen = input().split()
cH = Counter(sangguen)
M = int(input())
for test in input().split():
    print(cH[test],end=" ")