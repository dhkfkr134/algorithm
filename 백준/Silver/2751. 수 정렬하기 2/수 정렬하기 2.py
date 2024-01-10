# 1. 입력값이 10^6이므로 O(n)~O(nlogn)정도로 풀어야 한다.
# 2. 버블정렬 & 삽입정렬 & 선택정렬은 n2의 시간복잡도이다
# 3. 내장되어있는 sor()는 최악, 평균이 nlogn의 시간복잡도이므로 사용해보자
N = int(input())
arr = []
for _ in range(N):
   arr.append(int(input()))
arr.sort()
for i in range(N):
    print(arr[i])