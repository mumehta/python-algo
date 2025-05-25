from random import choice

tools = ["hammer", "screwdriver", "pliers",
         "drill", "saw", "wrench", "nail", "chisel"]
count = [quantity for quantity in range(100, 2000, 100)]


def get_tool():
  return choice(tools)


def get_count():
  return choice(count)


__all__ = ["tools", "count", "get_tool", "get_count"]
