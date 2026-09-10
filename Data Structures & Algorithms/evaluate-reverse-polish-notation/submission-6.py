import operator

class Stack:
    def __init__(self):
        self.mystack: List[str] = []

    def push(self, val: str) -> None:
        self.mystack.append(val)

    def pop(self) -> str|None:
        if len(self.mystack) < 1:
            return 0
        return self.mystack.pop()
    
    def peek(self) -> str|None:
        if len(self.mystack) < 1:
            return 0
        return self.mystack[-1]

    def size(self) -> int:
        return len(self.mystack)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = Stack()
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        if len(tokens) < 2:
            return int(tokens[-1])

        valueleft: int = 0
        valueright: int = 0
        for item in tokens:
            if item in ops:
                valueright = int(mystack.pop())
                valueleft = int(mystack.pop())
                mystack.push(ops[item](valueleft,valueright))
            else:
                mystack.push(item)
        return int(mystack.peek())

             

        