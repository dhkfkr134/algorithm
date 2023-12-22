# 10진법 변환은 입력받은 숫자의 자릿수마다 0,1,2,3,4...제곱을 한다는 것이 포인트다.
# 그리고 문자일 경우 적절하게 숫자로 변환하는 것도 포인트
N,B = input().split()
B = int(B)
result = 0
leng = len(N)
for j in range(leng):
    seng = leng-j-1
    result += int(N[j]) * (B**seng) if B <= 10 or ord(N[j]) < 64 else (ord(N[j]) - 55) * B**seng
print(result)
