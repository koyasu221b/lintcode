class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return len(self.min_stack) == 0

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if not self.is_empty():
            self.min_stack.append(min(number, self.min_stack[-1]))
        else:
            self.min_stack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if not self.is_empty():
            top = self.stack.pop()
            self.min_stack.pop()
            return top

    def min(self):
        # return the minimum number in stack
        if not self.is_empty():
            return self.min_stack[-1]

