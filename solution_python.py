class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = []
        self.undone = []

    def add(self, num: int):
        self.stack.append(num)
        self.value += num

    def subtract(self, num: int):
        self.stack.append(-1 * num)
        self.value -= num

    def undo(self):
        if self.stack:
            self.undone.append(self.stack.pop())
            self.value -= self.undone[-1]

    def redo(self):
        if self.undone:
            self.stack.append(self.undone.pop())
            self.value += self.stack[-1]

    def bulk_undo(self, steps: int):
        while self.stack and steps > 0:
            self.undone.append(self.stack.pop())
            self.value -= self.undone[-1]
            steps -= 1

    def bulk_redo(self, steps: int):
        while self.undone and steps > 0:
            self.stack.append(self.undone.pop())
            self.value += self.stack[-1]
            steps -= 1
