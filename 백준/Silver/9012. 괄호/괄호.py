# 클래스 초기화자, 생성자... 안쓰면 필드 공유함///
import sys

class Stack:

    stack_list = []
    size = 0

    def __new__(cls):
        return super().__new__(cls)

    def push(self, x):
        self.stack_list.append(x)
        self.size += 1
        return 0

    def pop(self):
        if self.is_empty():
            return -1
        result = self.peek()
        self.stack_list.pop()
        self.size -= 1
        return result

    def is_empty(self):
        return not bool(self.size)

    def peek(self):
        if self.size:
            return self.stack_list[-1]
        return -1


input = sys.stdin.readline
N = int(input())
for i in range(N):
    result = "YES"
    stack = Stack()
    for v in input().rstrip():
        if v == '(':
            stack.push(v)
            continue
        else:
            if stack.pop() == -1:
                result = "NO"
    if stack.is_empty():
        print(result)
    else:
        print("NO")


