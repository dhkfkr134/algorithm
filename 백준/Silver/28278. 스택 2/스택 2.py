# list로 stack 구현해보기
import sys

class Stack:

    stack_list = []
    size = 0

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
        if self.size:
            return 0
        else:
            return 1

    def peek(self):
        if self.size:
            return self.stack_list[len(self.stack_list)-1]
        return -1
input = sys.stdin.readline
stack = Stack()
N = int(input())
for i in range(N):
    c = input()
    x = 0
    if c[0] == '1':
        c, x = map(int, c.split())
    else:
        c = int(c)
    if c == 1:
        stack.push(x)
    elif c == 2:
        print(stack.pop())
    elif c == 3:
        print(stack.size)
    elif c == 4:
        print(stack.is_empty())
    else:
        print(stack.peek())