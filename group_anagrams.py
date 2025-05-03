'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''

from collections import defaultdict

def sorted_string(input):
    return ''.join(sorted(input))

strs = ["act", "pots", "tops", "cat", "stop", "hat"]

# Dictionary to group anagrams
anagram_groups = defaultdict(list)

for s in strs:
    key = sorted_string(s)
    anagram_groups[key].append(s)

# Get the grouped lists
output = list(anagram_groups.values())
print(output)

