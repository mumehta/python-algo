from any_random import get_tool, get_count


class HashTable:
  def __init__(self, size=7):
    self.data_map = [None] * size

  def __str__(self):
    return "\n".join(f"{i}: {slot}" for i, slot in enumerate(self.data_map))

  def __hash(self, key):
    my_hash = 0
    for letter in key:
      my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
    return my_hash

  def print_table(self):
    for i, val in enumerate(self.data_map):
      if val:
        for k, v in val:
          print(f"{i}: {k} -> {v}")
      else:
        print(f"{i}: None")

  def set_item(self, key, value):
    index = self.__hash(key)
    if self.data_map[index] is None:
      self.data_map[index] = []
    self.data_map[index].append([key, value])

  def get_item(self, key):
    index = self.__hash(key)
    if self.data_map[index] is not None:
      for i in range(len(self.data_map[index])):
        if self.data_map[index][i][0] == key:
          return self.data_map[index][i][1]
    return None

  def has_key(self, key):
    return self.get_item(key) is not None

  def keys(self):
    tool_list = []
    for index, slot in enumerate(self.data_map):
      if slot is not None:
        for key, _ in slot:
          tool_list.append(key)
    return tool_list


warehouse = HashTable()
tools = []

# add one tool at a time in hash table
for i in range(10):
  tool = get_tool()
  if tool not in tools:
    tools.append(tool)
    warehouse.set_item(tool, get_count())
warehouse.print_table()

tool = get_tool()
qty = warehouse.get_item(tool)
if qty is not None:
  print(f"In warehouse, we search for {tool} and have {qty} items.")
else:
  print(f"{tool} not found in warehouse.")

all_warehouse_tools = warehouse.keys()
print(f"All tools we have ...")
for _, tool in enumerate(all_warehouse_tools):
  print(tool, end=' ')
