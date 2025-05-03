'''
Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

'''
words = ["mass","as","hero","superhero"]
words = sorted(words)

output = []
for i, word in enumerate(words):
  tmp_words = words[i+1:]
  for t in tmp_words:
    if word in t:
      output.append(word)
  
print(output)
