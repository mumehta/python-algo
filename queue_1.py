class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Queue:
  def __init__(self, value):
    new_node = Node(value)
    self.first = new_node
    self.last = new_node
    self.length = 1

  def print_elements(self):
    temp = self.first
    while temp:
      print(temp.value, end="->")
      temp = temp.next
    print("None")

  def enqueue(self, value):
    new_node = Node(value)
    if self.length > 0:
      self.last.next = new_node
      self.last = new_node
    else:
      self.first = new_node
      self.last = new_node
    self.length += 1

  def dequeue(self):
    if self.length == 0:
      print("Queue is empty.")
      return None

    temp = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = self.first.next
      temp.next = None
    self.length -= 1
    return temp

  def has_elements(self):
    return True if self.length > 0 else False


queue = Queue(7)
queue.enqueue(14)
queue.enqueue(21)
queue.print_elements()
while queue.has_elements():
  node = queue.dequeue()
  if node:
    print(f"Dequeued element: {node.value}")
queue.print_elements()
