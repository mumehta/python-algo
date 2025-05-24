class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:
  def __init__(self):
    self.top = None
    self.height = 0

  def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
    self.height += 1

  def pop(self):
    if self.top is None:
      return None
    temp = self.top
    self.top = temp.next
    temp.next = None
    self.height -= 1
    return temp

  def peek(self):
    if self.top is None:
      return None
    return self.top.value

  def is_empty(self):
    if self.top is None:
      return True
    return False

  def print_stack(self):
    temp = self.top
    while temp:
      print(temp.value, end="->")
      temp = temp.next
    print(None)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()         # Output: 30 → 20 → 10 → None
print(stack.pop().value)          # Output: 30
print(stack.peek())         # Output: 20
print(stack.is_empty())
