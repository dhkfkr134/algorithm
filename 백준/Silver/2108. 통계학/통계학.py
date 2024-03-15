import math
from collections import Counter

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

# 산술평균
print(round(sum(arr)/N))
# 중앙값
print(arr[math.floor(N/2)])
# 최빈값 - 여러개일 경우 작은거에서 2번째
cnt = Counter(arr)
if N is 1:
    print(arr[0])
else:
    if cnt.most_common(2)[0][1] == cnt.most_common(2)[1][1]:
        print(cnt.most_common(2)[1][0])
    else:
        print(cnt.most_common(1)[0][0])
# 범위
print(max(arr) - min(arr))

