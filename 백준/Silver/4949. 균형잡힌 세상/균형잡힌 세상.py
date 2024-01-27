import sys

class Stack:

    stack_list = []
    size = 0

    def __init__(self):
        self.stack_list = []
        self.size = 0

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

input = sys.stdin.readlines

lines = input()
lines.pop()

for line in lines:
    line = line.rstrip()
    stack = Stack()
    result = "yes"
    for alpha in line:
        if alpha in "([])":
            if alpha in "[(":
                stack.push(alpha)
            elif alpha in ']':
                if stack.peek() == '[':
                    stack.pop()
                else:
                    result = "no"
            elif alpha in ')':
                if stack.peek() == '(':
                    stack.pop()
                else:
                    result = "no"
    if stack.size > 0:
        result = "no"
    print(result)

