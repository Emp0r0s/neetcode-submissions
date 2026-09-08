class MinStack:

    def __init__(self):
        self.mystack: list[int] = []
        self.minstack: list[int] = []
        
    def push(self, val: int) -> None:
        self.mystack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        
    def pop(self) -> None:
        if not self.mystack:
            return
        if self.mystack.pop() == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        if not self.mystack:
            return None
        return self.mystack[-1]
        

    def getMin(self) -> int:
        if not self.minstack:
            return None
        return self.minstack[-1]
        
