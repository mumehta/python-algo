class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)

    # Case 1: Empty tree
    if self.root is None:
      self.root = new_node
      return True

    temp = self.root
    while True:
      if value == temp.value:
        print(f"Duplicate value {value} not inserted.")
        return False  # or handle it as needed

      if value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left
      else:  # value > temp.value
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right

  def in_order_traversal(self):
    def traverse(node):
      if node:
        traverse(node.left)
        print(node.value, end=' ')
        traverse(node.right)
    traverse(self.root)
    print()

  def contains(self, value):
    temp = self.root
    while temp:
      if value < temp.value:
        temp = temp.left
      elif value > temp.value:
        temp = temp.right
      else:
        return True  # value == temp.value
    return False


bsd = BinarySearchTree()
bsd.insert(3)
bsd.insert(4)
bsd.insert(0)
bsd.insert(5)
bsd.in_order_traversal()
print(f"Contains 2: {bsd.contains(2)}")
print(f"Contains 5: {bsd.contains(5)}")
print(f"Contains 0: {bsd.contains(0)}")
print(f"Contains 4: {bsd.contains(4)}")
print(f"Contains 9: {bsd.contains(9)}")
