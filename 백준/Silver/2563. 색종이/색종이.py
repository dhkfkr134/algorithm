N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
result = 0
for i in range(N):
    x,y = map(int,input().split())
    for j in range(x-1,x+9):
        for k in range(y-1,y+9):
            if arr[j][k] == 0:
                result += 1
            arr[j][k] = 1
print(result)