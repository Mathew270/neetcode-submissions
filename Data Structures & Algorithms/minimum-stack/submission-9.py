class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = float('inf')

    def push(self, val: int) -> None:
        if val < self.minn:
            self.stack.append((val, val))
            self.minn = val
        else:
            self.stack.append((val, self.minn))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minn = self.stack[-1][1]
        else:
            self.minn = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
