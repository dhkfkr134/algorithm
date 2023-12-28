# 1. 입력값의 갯수 1~10000, 시간제한 1000ms -> 반복문 ok
# 2. 그냥 N까지 하나씩 찾으면서 K번째 약수 찾기
# 3. 찾았으면 출력
# 4. 못찾았으면 0출력
import sys
N, K = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break

if cnt != K:
    print(0)