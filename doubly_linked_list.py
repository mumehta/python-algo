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

  def prepend(self, value):  # Fixed name and cleaned logic
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1

  def insert(self, index, value):
    if index < 0 or index > self.length:
      print("Invalid index to insert value. Exiting")
      return

    if index == 0:
      self.prepend(value)
      return
    if index == self.length:
      self.append(value)
      return

    new_node = Node(value)
    temp = self.head
    for _ in range(index):
      temp = temp.next

    new_node.prev = temp.prev
    new_node.next = temp
    temp.prev.next = new_node
    temp.prev = new_node
    self.length += 1

  def remove(self, index):
    if index < 0 or index >= self.length:
      print("Invalid index to remove value. Exiting")
      return

    if index == 0:
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next
        self.head.prev.next = None
        self.head.prev = None
      self.length -= 1
      return

    if index == self.length - 1:
      self.pop()
      return

    temp = self.head
    for _ in range(index):
      temp = temp.next

    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    temp.prev = None
    temp.next = None
    self.length -= 1

  def get(self, index):
    if index < 0 or index >= self.length:
      print("Invalid index to fetch value. Exiting")
      return

    if index == 0:
      return self.head
    if index == self.length - 1:
      return self.tail

    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def reverse(self):
    if not self.head or self.length == 1:
      return  # Nothing to reverse

    temp = self.head
    self.head = self.tail
    self.tail = temp

    current = self.head
    while current:
      # Swap next and prev
      current.prev, current.next = current.next, current.prev
      current = current.next  # because next and prev have been swapped

  def is_palindrome(self):
    start = self.head
    end = self.tail

    for _ in range(self.length // 2):
      if start.value != end.value:
        return False
      start = start.next
      end = end.prev

    return True


dll = DoublyLinkedList(3)
dll.pop()
dll.prepend(0)
dll.append(6)
dll.append(3)
dll.append(3)
dll.append(6)
dll.append(0)

dll.print_doubly_linked_list()
is_dll_palindrom = dll.is_palindrome()
print(f"Node list is palindrom: {is_dll_palindrom}")
