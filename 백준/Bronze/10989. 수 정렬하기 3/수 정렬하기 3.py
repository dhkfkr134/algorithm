# 1. 입력값이 10^7이므로 내장 sort()를 돌려도 2*10^8근처가 나온다
# 2. 공간 복잡도도 생각해야한다. 동적으로 list의 크기를 늘리다 보면 작은 값에서는 상관없는데
#       10000정도에 8MB제한이면 걸릴수도? -> 정적배열을 만들어 준다.
# 3. hash의 개념을 사용해서 for문 한방에 index값에 순서대로 매핑시켜버리자.

import sys

n = int(sys.stdin.readline())
num = [0] * 10001

# num[1]이 1이면 1이 1개 이런식으로 알아서 순차적으로 매핑된다.
for _ in range(n):
    num[int(sys.stdin.readline())] += 1

# 순서대로 출력하면 끝
for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)