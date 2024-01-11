# 세상엔 참 똑똑한 사람이 많다. 나도 중복처리하자마자
# set과 dict가 떠오르긴 했는데 어떻게 할지 몰라서 직관적인 방법으로 바꾸었다.
# 그러나 할 수 있었다.
# 일단 맨처음상태의 arr이 있고, 중복처리와 오름차순을 적용한 arr2가 있다.
# 다음 vi마다 v'i를 매핑한 dic이 있고
# arr에서 dic을 통해서 v'i를 꺼낼 수 있다.
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')
