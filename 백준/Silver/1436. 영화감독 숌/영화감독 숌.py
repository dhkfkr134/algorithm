# N이 10000일때 5*10^6안쪽의 실행으로 끝낼수 있다.
N = int(input())

i = 0
N_cnt = 0
while True:
    i += 1
    if "666" in str(i):
        N_cnt += 1
        if N == N_cnt:
            print(i)
            break