import sys
lines = sys.stdin.readlines()
lines.pop()
higher = 0

for line in lines:
    higher = max(higher, int(line))
higher = (higher*2)+1
isprime = [1]*higher
for i in range(2,int(higher**0.5)+1):
    if isprime[i]:
        for j in range(i*2,higher,i):
            isprime[j] = 0

for line in lines:
    n = int(line)
    count = 0
    for i in range(n+1,2*n+1):
        if isprime[i]:
            count += 1
    print(count)