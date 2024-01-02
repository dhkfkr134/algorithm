# 1. 시간 제한 1초 입력값범위 1<= N <= 10,000,000
# 2. O(n)아래
# 3. 소인수분해에서 N/2이상은 for문돌리는게 무의미하다고 판단
# 4. 소수일경우를 대비해서 cnt로 소수를 판별하고 N값그대로 출력
import sys, math
N = int(sys.stdin.readline())
cnt = 0
result = N
for i in range(2, math.ceil(N/2)+1):
    while N % i == 0:
        print(i)
        N = N // i
        cnt += 1
if cnt == 0:
    if result != 1:
        print(result)