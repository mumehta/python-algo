'''
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
'''
from collections import defaultdict


def get_longest_sequence(nums):
  num_set = set(nums)
  longest = 0
  for n in num_set:
    # Only start counting if n is the beginning of a sequence
    if n - 1 not in num_set:
      current = n
      length = 1
      while current + 1 in num_set:
        current += 1
        length += 1
      longest = max(longest, length)
  return longest


nums = [3, 20, 4, 10, 2, 4, 5]
longest_sequence = get_longest_sequence(nums)
print(f"The longest sequence is {longest_sequence}")
