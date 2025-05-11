'''
3Sum
=====
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

# import random

# random_numbers = [random.randint(0,9) for _ in range(7)]

# print(random_numbers)

# random_numbers = sorted(random_numbers)
# print(random_numbers)

numbers = [0, 1, 3, 4, 7, 7, 9]

target = 12

def three_sum(numbers, target):
  numbers = sorted(numbers)
  result = set()
  for i in range(len(numbers) - 2):
    left = i+1
    right = len(numbers) - 1

    while left < right:
      sum = numbers[i] + numbers[left] + numbers[right]
      if (sum == target):
        result.add(tuple([numbers[i], numbers[left], numbers[right]]))
        left = left +1
        right = right -1
      elif sum < target:
        left = left +1
      else:
        right = right -1
  return list(result)


print(three_sum(numbers, target))
