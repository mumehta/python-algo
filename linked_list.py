from collections import defaultdict

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

  def print_linked_list(self, horizontal = False):
    temp = self.head
    if temp is not None:
      while temp.next is not None:
        if not horizontal:
          print(temp.value)
        else:
          print(temp.value, end=' ')
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

  def remove_duplicate_from_sorted_list(self):
    temp = self.head
    pre = self.head
    while temp and temp.next:
      pre = temp
      temp = temp.next
      if temp.value == pre.value:
        print(f"duplication found {temp.value}")
        pre.next = temp.next

  def remove_duplicate(self):
    temp = self.head
    seen = set()
    seen.add(temp.value)
    while temp and temp.next:
      if temp.next.value in seen:
        temp.next = temp.next.next
      else:
        seen.add(temp.next.value)
        temp = temp.next

  def binary_to_decimal(self):
    prev = 0
    total = 0
    temp = self.head
    while temp:
      total = (2 * prev) + temp.value
      prev = total
      temp = temp.next
    return total
  
  def partition_linked_list(self, value):
    before_list = Linked_List(0)
    after_list = Linked_List(0)
    before = before_list.head
    after = after_list.head
    current = self.head
    while current:
      next_node = current.next
      current.next = None
      if current.value < value:
        before.next = current
        before = before.next
      else:
        after.next = current
        after = after.next
      current = next_node
    before.next = after_list.head.next
    self.head = before_list.head.next
    self.tail = after if after.next is None else self.tail

  def reverse_between(self, left, right):
    if not self.head or left == right:
        return

    dummy = Node(0)
    dummy.next = self.head
    prev = dummy

    # Step 1: Reach node at position (left - 1)
    for _ in range(left - 1):
        prev = prev.next

    # Step 2: Reverse the sublist
    reverse_start = prev.next
    current = reverse_start.next

    for _ in range(right - left):
        temp = current.next
        current.next = prev.next
        prev.next = current
        reverse_start.next = temp
        current = temp

    # Step 3: Update head if needed
    self.head = dummy.next


linked_list = Linked_List(1)
linked_list.append(3)
linked_list.append(8)
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.append(3)
# my_linked_list.append(22)
# my_linked_list.append(66)
# my_linked_list.append(4)
# my_linked_list.append(44)
# my_linked_list.prepend(0)
# my_linked_list.append(66)
# my_linked_list.append(88)

print("Original linked list ... ")
linked_list.print_linked_list(horizontal=True)

# partition_at = 5
# linked_list.partition_linked_list(partition_at)

# print(f"Partitioned linked list at {partition_at} is:")
# linked_list.print_linked_list(horizontal=True)

left = 2
right = 5
print(f"reverse linked list between {left} and {right}")
linked_list.reverse_between(left, right)
linked_list.print_linked_list(horizontal=True)