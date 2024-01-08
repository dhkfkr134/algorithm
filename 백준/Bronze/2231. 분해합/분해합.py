# 그냥 1000000가지 경우 다 구함...
# 근데 언제까지가 1000000까지인지 몰라서 대충 N의 생성자는 N보다 작으니깐 N까지로 돌림
# 10의 자리 단위로 나눌때 생각해두기

N = int(input())
for i in range(N+1):
    result = sum(map(int, str(i)))
    result += i
    if result == N:
        print(i)
        break
    if i == N:
        print(0)