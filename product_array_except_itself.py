'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in  O(n)
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''


def product_all_except_itself(nums):
  n = len(nums)
  left = [1] * n
  for i in range(1, n):
    left[i] = left[i - 1] * nums[i - 1]
  right = [1] * n
  for i in range(n - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]
  output = [x * y for x, y in zip(left, right)]
  return output


input = [-1, 0, 1, 2, 3]
output = product_all_except_itself(input)
print(f"product array except itself is {output}")
