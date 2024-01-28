import sys
from _collections import deque
input = sys.stdin.readline

N = int(input())
students = deque(map(int, input().split()))

number = 1
stack = []

while number <= N:
    if students and number == students[0]:
        number += 1
        students.popleft()
    elif stack and number == stack[-1]:
        number += 1
        stack.pop()
    else:
        if not students:
            break
        else:
            cur = students.popleft()
            stack.append(cur)

if number > N:
    print('Nice')
else:
    print('Sad')