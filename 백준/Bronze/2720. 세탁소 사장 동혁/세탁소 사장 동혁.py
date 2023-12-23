T = int(input())
for i in range(T):
    Q = D = N = P = 0
    C = int(input())
    while True:
        if C >= 25:
            Q = C // 25
            C = C % 25
        elif C >= 10:
            D = C // 10
            C = C % 10
        elif C >= 5:
            N = C // 5
            C = C % 5
        else:
            P = C
            break
    print(f'{Q} {D} {N} {P}')