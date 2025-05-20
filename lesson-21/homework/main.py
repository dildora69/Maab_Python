
import pandas as pd
# import matplotlib.pyplot as plt
#
# # Given Data
# data1 = {
#     'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
#     'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
#     'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
# }
#
# df1 = pd.DataFrame(data1)
#
# # Exercise 1: Average grade for each student
# df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
# print("Average grades for each student:")
# print(df1[['Student_ID', 'Average']])
#
# # Exercise 2: Student with the highest average grade
# max_avg = df1['Average'].max()
# top_student = df1[df1['Average'] == max_avg]
# print("\nStudent with the highest average grade:")
# print(top_student[['Student_ID', 'Average']])
#
# # Exercise 3: Add 'Total' column
# df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
# print("\nData with Total marks:")
# print(df1)
#
# # Exercise 4: Bar chart for average grades per subject
# subject_avgs = df1[['Math', 'English', 'Science']].mean()
#
# plt.figure(figsize=(6, 4))
# subject_avgs.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
# plt.title('Average Grades in Each Subject')
# plt.ylabel('Average Grade')
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()



# Given Data
# data2 = {
#     'Date': pd.date_range(start='2023-01-01', periods=10),
#     'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
#     'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
#     'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
# }
#
# df2 = pd.DataFrame(data2)
#
# # Exercise 1: Total sales for each product
# total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
# print("Total sales for each product:")
# print(total_sales)
#
# # Exercise 2: Date with highest total sales
# df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
# max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
# print("\nDate with highest total sales:")
# print(max_sales_date)
#
# # Exercise 3: Percentage change in sales from previous day
# pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
# print("\nPercentage change in sales for each product:")
# print(pct_change)
#
# # Exercise 4: Line chart of sales trends
# plt.figure(figsize=(8, 5))
# plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
# plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='o')
# plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='o')
# plt.title('Sales Trends Over Time')
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()


data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Average salary for each department
avg_salary = df3.groupby('Department')['Salary'].mean()
print("Average salary per department:\n", avg_salary)

# Exercise 2: Employee with most experience
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nMost experienced employee:\n", most_experienced[['Name', 'Experience (Years)']])

# Exercise 3: New column for % salary increase from minimum
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("\nDataFrame with Salary Increase column:\n", df3[['Name', 'Salary', 'Salary Increase']])

# Exercise 4: Bar chart of employee distribution across departments
dept_counts = df3['Department'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(dept_counts.index, dept_counts.values, color='skyblue')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.show()


data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Total revenue
total_revenue = df4['Total_Price'].sum()
print("Total Revenue:", total_revenue)

# Exercise 2: Most ordered product









