# %대신 비트연산 사용하기
N = int(input())
# 대각선방향을 한줄단위로 본다.
line = 1
x = y = 0
# N값의 위치가 몇번째 줄인지 확인한다. 한 line에 들어가는 값이 line의 크기과 같기때문에 가능
while N > line:
    N -= line
    line += 1
# 줄이 짝수일때는 y값이 작아지고 x값이 커지는 로직
if line & 1 == 0:
    x = N
    y = line-N+1
# 홀수일때는 반대
elif line & 1 == 1:
    x = line-N+1
    y = N
print(f'{x}/{y}')