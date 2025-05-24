'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''


def get_pascal_triangle(numRows):
  results = []

  if numRows == 0:
    return results

  firstRow = [1]
  results.append(firstRow)

  if numRows == 1:
    return results

  for n in range(1, numRows):
    prevRow = results[n - 1]

    row = []
    row.append(1)
    for j in range(0, n - 1):
      row.append(prevRow[j] + prevRow[j + 1])
    row.append(1)

    results.append(row)
  return results


results = get_pascal_triangle(5)
print(results)
