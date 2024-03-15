# 재귀연습 - 피보나치
def solution(num):

    if num is 0:
        return 0
    elif num is 1:
        return 1
    else:
        return solution(num - 2) + solution(num - 1)


print(solution(int(input())))