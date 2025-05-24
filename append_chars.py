'''
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
'''

sing = "coaching"
ting = "coding"

i = 0
j = 0

while i < len(sing) and j < len(ting):
  if ting[j] == sing[i]:
    j = j + 1
  i = i + 1

if i == len(sing) and j < len(ting):
  count = len(ting) - j

print(f"THe number of characters to be appended would be {count}")
