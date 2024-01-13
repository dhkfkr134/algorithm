# 1. A,B의 원소값이 문자열로 들어갔지만, 비교만 가능하면되니깐 상관없다.
# 3. 파이썬은 다 알고만 있으면 참 편리하다
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(input().split())
B = set(input().split())

result = set.difference(A|B, set.intersection(A,B))

print(len(result))

