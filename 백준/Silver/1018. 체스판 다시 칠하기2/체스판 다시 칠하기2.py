# 50*50사이즈의 보드에 8*8의 체스판 두종류를 모두 대가면서 가장조금 바꿔도되는것을
# 하나하나 모두 찾는다.
import sys
#체스판 준비
N , M = map(int,input().split())
board = list((sys.stdin.readline().split()) for _ in range(N))
line1 = ["B","W","B","W","B","W","B","W"]
line2 = ["W","B","W","B","W","B","W","B"]
chessBoardW = [0]*8
chessBoardB = [0]*8
result = 0
for i in range(8):
    if i & 1 == 0:
        chessBoardB[i] = line1
        chessBoardW[i] = line2
    else:
        chessBoardB[i] = line2
        chessBoardW[i] = line1
# 체스판을 직접대가면서 모든케이스 비교 최대 43*43*8*8*2의 실행
for i in range(N - 7):
    for j in range(M - 7):
        Bnum = 0
        Wnum = 0
        for x in range(8):
            for y in range(8):
                if board[i+x][0][j+y] == chessBoardB[x][y]:
                    Bnum += 1
                elif board[i+x][0][j+y] == chessBoardW[x][y]:
                    Wnum += 1
        result = max(result, max(Bnum, Wnum))
print(64 - result)