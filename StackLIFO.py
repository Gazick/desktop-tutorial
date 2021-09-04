class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            return self.values.pop()

    def peek(self):
        if len(self.values) == 0:
            print("Empty Stack")
            return
        else:
            return self.values[-1]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)
