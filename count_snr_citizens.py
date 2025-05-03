'''
You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.

Example 1:

Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
Output: 2
Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
'''

passengers =  ["7868190130M7522","5303914400F9211","9273338290F4010"]

senior_citizen_age = 60
senior_citizen = 0
for passenger in passengers:
  phone = passenger[:10]
  sex = passenger[10:11]
  age = passenger[11:13]
  seat = passenger[13:]
  print(f"phone: {phone}, sex: {sex}, age: {age} and seat: {seat}")
  if int(age) > senior_citizen_age:
    senior_citizen +=1

print(f"Senior citizens are: {senior_citizen}")
