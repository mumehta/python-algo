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
    return True

  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.tail = new_node
    else:
      new_node.next = self.head
    self.head = new_node
    self.length += 1
    return True

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
    
  def pop_first(self):
    if self.length == 0:
      return None
    else:
      temp = self.head
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        self.head = temp.next
        temp.next = None
      self.length -= 1
      return temp

  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    else:
      if index == 0:
        return self.pop_first()
      if index == self.length - 1:
        return self.pop()
      cur = self.get(index - 1)
      temp = cur.next
      cur.next = temp.next
      temp.next = None
      self.length -= 1
      return temp

  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    before = None
    after = temp.next
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after

      
  def get_middle_node(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow

  def has_loop(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False

  def get_kth_element_from_end(self, index_from_end):
    slow = self.head
    fast = self.head
    if index_from_end <0 or index_from_end > self.length:
      return None
    for _ in range(index_from_end):
      fast = fast.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next
    return slow

my_linked_list = Linked_List(4)
my_linked_list.append(22)
my_linked_list.append(44)
my_linked_list.prepend(0)

my_linked_list.print_linked_list()
node = my_linked_list.get_kth_element_from_end(0)
print(f"node is: {node.value}")

print("== Reverse the link list === ")
my_linked_list.reverse()
my_linked_list.print_linked_list()
print("=== done ===")