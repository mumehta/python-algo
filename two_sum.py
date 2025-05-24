# import random

# random_numbers = [random.randint(0,9) for _ in range(7)]

# print(random_numbers)

# random_numbers = sorted(random_numbers)
# print(random_numbers)

numbers = [0, 1, 3, 4, 7, 7, 9]

target = 7


def two_sums(numbers, target):
  seen = set()
  result = set()

  for num in numbers:
    complement = target - num
    if complement in seen:
      result.add(tuple(sorted((num, complement))))
    seen.add(num)
  return [list(pair) for pair in result]


print(two_sums(numbers, target))
