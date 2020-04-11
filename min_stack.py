
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif self.getMin() >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.getMin():
            self.min_stack.pop()
        return num

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]


