import pandas as pd
import numpy as np

# data = {
#     'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
# }
#
# df = pd.DataFrame(data)
#
# # Rename columns using a function
# df.columns = [col.lower().replace(" ", "_") for col in df.columns]
#
# # Print first 3 rows
# print("First 3 rows:")
# print(df.head(3))
#
# # Mean age
# print("Mean age:")
# print(df['age'].mean())
#
# # Select only 'first_name' and 'city'
# print("Name and City columns:")
# print(df[['first_name', 'city']])
#
# # Add a new column 'Salary' with random values
# df['salary'] = np.random.randint(3000, 7000, size=4)
#
# # Display summary statistics
# print("Summary statistics:")
# print(df.describe())


# 2

# import pandas as pd
#
# # Create DataFrame
# data = {
#     'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
#     'January': [1200, 200, 300, 150],
#     'February': [1300, 220, 320, 160],
#     'March': [1400, 240, 330, 170],
#     'April': [1500, 250, 350, 180]
# }
#
# expenses = pd.DataFrame(data)
#
# # Set 'Category' as index
# expenses = expenses.set_index('Category')
#
# # Max per category
# print("Maximum expense per category:")
# print(expenses.max(axis=1))
#
# # Min per category
# print("Minimum expense per category:")
# print(expenses.min(axis=1))
#
# # Average per category
# print("Average expense per category:")
# print(expenses.mean(axis=1))

