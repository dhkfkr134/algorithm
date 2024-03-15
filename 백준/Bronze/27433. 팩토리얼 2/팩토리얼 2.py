def solution(num):
    if num is 0:
        return 1
    return num * solution(num-1)

print(solution(int(input())))