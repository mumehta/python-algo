'''
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.

 Example 1:
Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
'''

s = "zaz"

sum = 0
for i in range(len(s)):
  if i + 1 < len(s):
    n = abs(ord(s[i + 1]) - ord(s[i]))
    sum = sum + n
print(sum)
