import re

text = "Sample text with phone number +91 83278-20802"
phone_numbers = re.findall(r'\+\d{2} \d{5}-\d{5}', text)

print(phone_numbers)

'''
    \+: This matches the plus sign '+' literally. In regular expressions, '+' is a special character, so it needs to be escaped with a backslash to be treated as a literal character.

    \d{2}: This matches one or two digits. \d represents any digit (0-9), and {1,2} specifies that there should be either one or two digits.

    \d{5}-\d{5}: This matches five digits, followed by a hyphen '-', and then five more digits.
    
    So, the regular expression is looking for phone numbers in the format of "+XX XXXX-XXXX," where 'X' represents a digit.
'''



data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_data = sorted(data)  # Sort in ascending order
sorted_data_desc = sorted(data, reverse=True)  # Sort in descending order


sales = [
    {"product": "A", "amount": 100},
    {"product": "B", "amount": 150},
    {"product": "A", "amount": 75},
    {"product": "C", "amount": 200}
]

from collections import defaultdict

total_sales_by_category = defaultdict(int)
for sale in sales:
    total_sales_by_category[sale["product"]] += sale["amount"]

print(total_sales_by_category)