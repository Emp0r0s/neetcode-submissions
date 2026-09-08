class Stack:
    
    def __init__(self):
        self.stack: list[Any] = []

    def size(self) -> Any:
        return len(self.stack)

    def pop(self) -> Any:
        if self.size() < 1:
            return None
        return self.stack.pop()

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def peek(self) -> Any:
        if self.size() < 1:
            return None
        return self.stack[-1]


class Solution:
    def isValid(self, s: str) -> bool:
        mystack = Stack()
        mapping = {")":"(", "}":"{", "]":"["}

        if len(s) == 1:
            return False

        for bracket in s:
            if bracket == ")" or bracket == "}" or bracket == "]":
                if mapping.get(bracket) == mystack.peek():
                    mystack.pop()
                else:
                    return False
            else:
                mystack.push(bracket)

            
        return mystack.size() == 0
        