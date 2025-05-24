class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None


class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_doubly_linked_list(self):
    temp = self.head
    while temp:
      print(temp.value, end=' ')
      temp = temp.next
    print()

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1

  def pop(self):
    if self.length == 0:
      print("Doubly linked list is empty, nothing to return...")
      return None

    temp = self.tail

    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = temp.prev
      self.tail.next = None
      temp.prev = None

    self.length -= 1
    return temp
