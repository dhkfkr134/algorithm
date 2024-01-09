import math
check = 0
N = int(input())
for i in range(math.ceil(N / 5),-1,-1):
    for j in range(math.ceil(N/3)+1):
        if 5*i + 3*j == N:
            print(i+j)
            check += 1
            break
    if check != 0:
        break
if check == 0:
    print(-1)
