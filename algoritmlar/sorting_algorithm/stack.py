class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        """Bo'sh ekanligini tekshirish """
        return len(self.stack) == 0

    def push(self, new_data):
        """Element qo'shish"""
        self.stack.append(new_data)
        return True

    def pop(self):
        """Element sug'urib olish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]

stack1 = Stack()

print(stack1.isEmpty())
stack1.push(6)
stack1.push(7)
stack1.push(8)
print(stack1.isEmpty())
print(stack1.peek())
print(stack1.pop())