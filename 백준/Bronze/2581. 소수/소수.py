# n,m은 10000이하의 자연수
# 대충 최대n^2이하로 만들어야하고 nlogn에 가깝게 해야될거 같다.
m = int(input())
n = int(input())
arr = []

for i in range(m, n+1):
    for j in range(2, i+1):
            if j == i:
                arr.append(i)
            if i % j == 0:
                break
                
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])