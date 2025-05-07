'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
'''

def list_to_string(lst):
    str = ""
    for i in lst:
        str = str+" "+i
    return str.strip()

def string_to_list(str):
    lst = str.split(" ")
    return lst

input = ["neet","code","love","you"]
str = list_to_string(input)
output = string_to_list(str)
# print(f"The list {input} converted to string {str}")
# print(f"The string {str} converted back to list {output}")


def encode(strs):
    return ''.join(f'{len(s)}#{s}' for s in strs)

def decode(s):
    i = 0
    result = []
    while i < len(s):
        j = s.find('#',i)
        length = int(s[i:j])
        i = j + 1
        result.append(s[i:i + length])
        i += length
    return result

input = ["neet","code","love","you"]
encoded = encode(input)
print(encoded)
decoded = decode(encoded)
print(decoded)