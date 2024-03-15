from collections import Counter

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

dictionary = Counter(arr)

# 1. 가장많이 등장한 것이 먼저 출력(value값 기준 내림차순)
# 2. 길이가 긴단어 먼저 출력(key의 길이 기준 내림차순)
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
sorted_items = sorted(dictionary.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for key,value in sorted_items:
    # 4. key 길이가 M이하면 필요없음
    if len(key) >= M:
        print(key)