# Filtering Data with List Comprehensions:
# Suppose you have a list of numbers, and you want to create a new list with only the even numbers:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)



# Sorting Data:
# You can sort a list of elements in ascending or descending order:

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_data = sorted(data)  # Sort in ascending order
sorted_data_desc = sorted(data, reverse=True)  # Sort in descending order
print(sorted_data, sorted_data_desc)



# Mapping and Transformation:
# Let's say you have a list of temperatures in Celsius and you want to convert them to Fahrenheit:

celsius_temperatures = [0, 25, 30, 35]
fahrenheit_temperatures = [(c * 9/5) + 32 for c in celsius_temperatures]
print(fahrenheit_temperatures)



# Grouping and Aggregation:
# If you have a list of sales transactions and you want to calculate the total sales per product category:

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



# Filtering Data with Pandas:
# For more complex data manipulation and analysis, you can use the Pandas library. Suppose you have a CSV file with sales data:

import pandas as pd

# Read the data from a CSV file
df = pd.read_csv("sales_data.csv")
df2 = pd.read_csv("sales_data.csv")
# Filter rows where sales are greater than 1000
high_sales = df[df["sales"] > 1000]

# Calculate the mean sales per category
mean_sales_by_category = df.groupby("category")["sales"].mean()
print(mean_sales_by_category)

# Joining Data with Pandas:
# You can join data from multiple DataFrames based on a common key, like an ID or a date:

# Join two DataFrames based on a common column
merged_data = pd.merge(df, df2, on="common_column")
print(merged_data)



# Data Cleaning and Missing Value Handling:
# Data often contains missing or inconsistent values. Pandas can help you clean and preprocess data:

import pandas as pd

# Load a dataset with missing values
data = pd.read_csv("data_with_missing_values.csv")

# Drop rows with missing values
cleaned_data = data.dropna()

# Fill missing values with a specific value
data["column_name"].fillna(0, inplace=True)



# Text Data Processing:
# If you have textual data and want to perform text analysis, you can use regular expressions to extract information:
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



# Data Aggregation:
# You can aggregate data to calculate statistics like sum, mean, and counts:

import pandas as pd

# Group data by a column and calculate the sum and mean
df = pd.read_csv("sales_data.csv")
total_sales = df.groupby("product")["sales"].sum()
average_price = df.groupby("category")["price"].mean()



# Time Series Data Analysis:
# If you're working with time series data, you can use libraries like Pandas and Matplotlib to analyze and visualize trends:

import pandas as pd
import matplotlib.pyplot as plt

# Read time series data
data = pd.read_csv("time_series_data.csv")

# Plot a time series
data.plot(x="year", y="estimate")
plt.show()



