class InvalidIndexError(Exception):
  def __init__(self, index, message="Invalid index provided."):
      self.index = index
      self.message = f"{message} Index: {index}"
      super().__init__(self.message)

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Linked_List:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    self.length += 1

  def print_linked_list(self):
    temp = self.head
    if temp is not None:
      while temp.next is not None:
        print(temp.value)
        temp = temp.next
      print(temp.value)
    else:
      print("Linked list is empty")

  def pop(self):
    if self.length == 0:
      return None
    else:
      temp = self.head
      pre = self.head
      while temp.next is not None:
        pre = temp
        temp = temp.next
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        self.tail = pre
        self.tail.next = None
      self.length -= 1
      return temp
      
  def insert(self, index, value):
    new_node = Node(value)

    if index < 0 or index > self.length:
      raise InvalidIndexError(index)
    
    if index == 0:
      return self.prepend(value)
    
    if index == self.length:
      return self.append(value)
    
    prev = self.head
    for _ in range(index - 1):
      prev = prev.next
    
    new_node.next = prev.next
    prev.next = new_node
    self.length += 1
    return True
    
my_linked_list = Linked_List(4)
my_linked_list.append(22)
my_linked_list.append(44)
my_linked_list.prepend(0)
# popped = my_linked_list.pop()
# print(popped.value)
# popped = my_linked_list.pop()
# print(popped.value)
# popped = my_linked_list.pop()
# print(popped.value)
# my_linked_list.print_linked_list()

my_linked_list.insert(3, 33)
my_linked_list.print_linked_list()