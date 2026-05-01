class MinStack:

    def __init__(self):
        self.stack_list = []
        self.min_stack = []
 
    def push(self, val: int) -> None:
        self.stack_list.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:#only pushes if min stack is empty or value is smaller
            self.min_stack.append(val)
    def pop(self) -> None:
        popped_val = self.stack_list.pop()
        if self.min_stack[-1] == popped_val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack_list[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]