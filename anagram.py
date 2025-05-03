'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

'''

s = "racecar"
t = "carrace"
t_list = list(t)

for i in range(len(s)):
  for j in range(len(t_list)):
    if t_list[j] == s[i]:
      t_list.pop(j)
      break

if len(t_list) == 0:
  print("s and t are anagram")
else:
  print("s and t are not anagrams")
