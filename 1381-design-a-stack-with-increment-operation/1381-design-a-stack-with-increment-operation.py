class CustomStack:
    def __init__(self, max_size):
        # Array to store stack elements
        self._stack = []
        # Index of the top element in the stack
        self._max_size = max_size

    def push(self, x):
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self):
        return self._stack.pop() if self._stack else -1

    def increment(self, k, val):
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val