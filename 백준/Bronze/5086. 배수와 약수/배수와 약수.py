import sys
lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    if A == 0:
        break
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")