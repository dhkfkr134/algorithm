N = int(input())
N -= 1
sub = 1
result = 1
while N > 0:
    N = N - sub
    if sub == 1:
        sub = 0
    sub += 6
    if N < 0:
        break
    result += 1
print(result)