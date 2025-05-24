'''
Valid Palindrome
=================
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.
'''

import re


def remove_non_alphanumeric(s):
  return re.sub(r'[^a-zA-Z0-9]', '', s).lower()


def palindrome_test(s):
  s_len = len(s)
  for i in range(s_len // 2):
    if s[i] != s[s_len - 1 - i]:
      return False
  return True


s = "Was it a car or a cat I saw?"
is_valid_palindrome = palindrome_test(remove_non_alphanumeric(s))
print(f'The given string {s} is a palindrome: {is_valid_palindrome}')
