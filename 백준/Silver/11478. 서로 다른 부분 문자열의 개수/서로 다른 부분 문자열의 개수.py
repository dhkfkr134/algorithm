# 1. S의 길이는 최대1000이니깐 이중for문쓰자
# 2. 브루트포스마냥 다 찾자
import sys
input = sys.stdin.readline

S = input().rstrip()
sett = set()
for i in range(1, len(S)+1):
    for j in range(len(S)-i):
        sett.add(S[j:j+i])
        if j == len(S)-i-1:
            sett.add(S[j+1:j+1+i])
sett.add(S)
print(len(sett))