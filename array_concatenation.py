'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.



Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
'''

import random
nums = [random.randint(0, 9) for _ in range(3)]

print(nums)
ans = []

for i in range(2 * len(nums)):
  if i < len(nums):
    ans.append(nums[i])
  else:
    ans.append(nums[i - len(nums)])

print(ans)
