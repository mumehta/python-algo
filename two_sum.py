import random

random_numbers = [random.randint(0,9) for _ in range(7)]

print(random_numbers)

output = []

target = 11

for i in range(len(random_numbers)):
  for j in range(i+1,len(random_numbers)):
    if random_numbers[i] + random_numbers[j] == target:
      print(f"Indices: {i}, {j} (Values: {random_numbers[i], random_numbers[j]})")
      found = True
      break
  if found:
    break
if not found:
  print("No two numbers add up to target")
