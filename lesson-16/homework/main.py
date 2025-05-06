import pandas as pd

employee = pd.read_csv('employee.csv')

print(employee.columns)

top_departments = employee['DEPARTMENT'].value_counts().head(5)

print(top_departments)