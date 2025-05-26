class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class HashTable:
  def __init__(self, size=7):
    self.data_map = [None] * size

  def __hash(self, animal):
    my_hash = 0
    for char in animal:
      my_hash = (my_hash + ord(char) * 23) % len(self.data_map)
    return my_hash

  def set_item(self, value):
    index = self.__hash(value)
    new_node = Node(value)
    if self.data_map[index] is not None:
      cur_node = self.data_map[index]
      while cur_node.next:
        cur_node = cur_node.next
      cur_node.next = new_node
    else:
      self.data_map[index] = new_node

  def print_table(self):
    for index, node in enumerate(self.data_map):
      if node:
        chain = []
        while node:
          chain.append(node.value)
          node = node.next
        print(f"{index}: {' -> '.join(chain)}")
      else:
        print(f"{index}: None")

  def has_item(self, value):
    index = self.__hash(value)
    temp = self.data_map[index]
    while temp:
      if value == temp.value:
        return True
      temp = temp.next
    return False

  def get_items(self):
    items = []

    for node in self.data_map:
      while node:
        items.append(node.value)
        node = node.next

    if items:
      print(*items)
    else:
      print("Hash table is empty. Nothing to print")


table = HashTable()
table.set_item("dog")
table.set_item("cat")
table.set_item("mouse")
table.print_table()
print(f"Table has dog: {table.has_item('dog')}")
print(f"Table has elephant: {table.has_item('elephant')}")
table.get_items()
