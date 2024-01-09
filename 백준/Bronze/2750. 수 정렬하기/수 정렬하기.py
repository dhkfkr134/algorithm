# 정렬 기본 문제이므로 삽입정렬을 사용했다.
# 내장함수 sort()는 나중에 사용하자
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
for i in arr:
    print(i)