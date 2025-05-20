import pandas as pd
import numpy as np
import requests
import json

# 1. 3x3x3 array

# a = np.random.rand(3, 3, 3)
# print(a)


# 2


# 2. import pandas as pd

# data = {
#     'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
# }
#
# df = pd.DataFrame(data)

# 2.1 rename column name
#
# df.columns = [col.lower().replace(" ", "_") for col in df.columns]
# print(df)


# 2.2 top 3 rows

# print(df.head(3))


# 2.3 mean Age

# age_mean = df['Age'].mean()
# print(age_mean)

# 2.4 Print only ' Name', 'City'
# print(df[['First Name', 'City']])

# 2.5 Add a new Column

# df['Salary'] = np.random.randint(1000, 5000, size=4)
# print(df)


# 2.6 Summary Statistics

# print(df.describe())




# 3. URL fetch data

# weather URl
# url = 'https://api.openweathermap.org/data/2.5/weather'
#
#
# parameters = {
#     'appid': '94a8f581728ac1908cf45d15f250d56e', # API from weather website
#     'lang': 'en',
#     'units': 'metric'
# }
#
# while True:
#     user_input = input('Please enter a City name to get its weather details: ')
#     parameters['q'] = user_input
#
#     try:
#         weather = requests.get(url, params=parameters).json()
#         name = weather['name']
#         temp = weather['main']['temp']
#         description = weather['weather'][0]['description']
#         timezone = weather['timezone']
# #
#         print(f'''In the City {name} now {description}
# Temperature: {temp} °C
# TimeZone: {timezone}''')
#
#     except Exception as e:
#         print('You Entered wrong City Name.')







# 4. NumPy

# lst = [10, 20, 30]
# a = np.array(lst)
# new_array = np.append(lst, np.arange(40, 100, 10))
# print(new_array)




# 5 Movie Recommendation System

url = 'http://www.omdbapi.com/?i=tt3896198&apikey=8f8a91c4'


parameters = {
    'appid': '8f8a91c4', # API from weather website
    'lang': 'en'
}

user_input = input('Please enter a Movie Title to find you latest Recommendations: ')
parameters['t'] = user_input
movie = requests.get(url, params=parameters).json()


title = movie['Title']
year = movie['Year']
rate = movie['Rated']
release_date = movie['Released']

print(f'''Recommended Movies:
        Title: {title}
        Year: {year}
        Movie Rated: {rate}
        Release Date: {release_date}
''')

print(movie)





