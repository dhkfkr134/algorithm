N,B = input().split()
B = int(B)
result = 0
leng = len(N)
for j in range(leng):
    seng = leng-j-1
    result += int(N[j]) * (B**seng) if B <= 10 or ord(N[j]) < 64 else (ord(N[j]) - 55) * B**seng
print(result)
