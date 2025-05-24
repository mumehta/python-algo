'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

 Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

'''

strs1 = ["flower", "flow", "flight"]
strs = ["cluster", "clue", "clutch", "club", "clumsy"]

strs = sorted(strs)

first = strs[0]
last = strs[-1]

result = []

for i in range(len(first)):
  if first[i] == last[i]:
    result.append(first[i])
  else:
    break

print(''.join(result))
