import pandas as pd

# 1

# df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1. Questions before 2014
# df['creationdate'] = pd.to_datetime(df['creationdate'])
# q1 = df[df['creationdate'].dt.year < 2014]

# 2. Score more than 50
# q2 = df[df['score'] > 50]

# 3. Score between 50 and 100
# q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. Questions answered by Scott Boston
# q4 = df[df['ans_name'] == 'Scott Boston']

# 5. Questions answered by these 5 users
# users = ['unutbu', 'jezrael', 'Warren Weckesser', 'Scott Boston', 'cs95']
# q5 = df[df['ans_name'].isin(users)]

# 6. Created between March 2014 and October 2014, answered by Unutbu, score < 5
q6 = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]

# 7. Score between 5–10 or viewcount > 10,000
q7 = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]

# 8. Not answered by Scott Boston
q8 = df[df['ans_name'] != 'Scott Boston']



# 3

titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Female Class 1 passengers aged 20–30
h3_1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]

# 2. Fare > 100
h3_2 = titanic_df[titanic_df['Fare'] > 100]

# 3. Survived and alone (no siblings/spouses or parents/children)
h3_3 = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# 4. Embarked from 'C' and paid > 50
h3_4 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# 5. Had both siblings/spouses and parents/children
h3_5 = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# 6. Aged ≤ 15 and didn't survive
h3_6 = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# 7. Cabin not null and fare > 200
h3_7 = titanic_df[
    titanic_df['Cabin'].notna() &
    (titanic_df['Fare'] > 200)
]

# 8. Odd-numbered PassengerId
h3_8 = titanic_df[titanic_df['PassengerId'] % 2 != 0]

# 9. Unique ticket numbers
h3_9 = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]

# 10. 'Miss' in name and Class 1
h3_10 = titanic_df[
    titanic_df['Name'].str.contains('Miss') &
    (titanic_df['Pclass'] == 1)
]




