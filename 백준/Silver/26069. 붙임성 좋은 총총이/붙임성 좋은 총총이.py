def findRainbowDancing():
    N = int(input())
    sett = {"ChongChong"}
    for _ in range(N):
        a, b = map(str,input().split())
        if a in sett:
            sett.add(b)
        elif b in sett:
            sett.add(a)
    return len(sett)
print(findRainbowDancing())



