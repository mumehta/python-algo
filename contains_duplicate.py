'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.
'''

import random

nums = [random.randint(0,9) for _ in range(0,4)]
print(nums)

duplicate = False
for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    if nums[j] == nums[i]:
      duplicate = True

print(duplicate)
    