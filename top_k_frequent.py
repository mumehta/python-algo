'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

'''
Attempt 1
from collections import defaultdict

nums = [5,5,5,6,6,7]
k=2

groups = defaultdict(list)
count = 0
for i in range(len(nums)):
    key = nums[i]
    groups[key].append(count+1)

output = []
counter = 0
for i in groups:
    if counter < k:
        counter = counter+1
        output.append(i)
    else:
        break

print(output)'''


from collections import Counter

def most_frequent_k(nums, k):
    freq_map = Counter(nums)
    most_common = freq_map.most_common(k)
    return [num for num, count in most_common]

nums = [7,7,7,8,8,9]
print(most_frequent_k(nums, 2))