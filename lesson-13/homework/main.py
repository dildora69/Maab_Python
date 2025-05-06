from datetime import datetime, timedelta
import re
from dateutil.relativedelta import relativedelta

# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.


# birth_date = input('Please enter your birthdate in a (dd/mm/yyyy):  ')
#
# date_obj = datetime.strptime(birth_date, "%d/%m/%Y")
# today = datetime.today()
#
# days = (today - date_obj).days
#
# year = days // 365
# left_days = days % 365
# months = left_days // 30
# days  = left_days % 30
#
# print(f'Years: {year}, month: {months}, days: {days}')


# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

# birth_date = input('Please enter your birthdate in a (dd/mm/yyyy):  ')
# birth = datetime.strptime(birth_date,  "%d/%m/%Y")
# today = datetime.today()
#
# next_birthday = birth.replace(year=today.year)
#
# if next_birthday < today:
#     next_birthday = next_birthday.replace(year=today.year+1)
#
# diff = relativedelta(next_birthday, today)
#
# print(f"Your next birthday is in {diff.months} month(s) and {diff.days} day(s).")
# print(next_birthday)


# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.


# current_date_time = input('Please enter current date and time in a (dd/mm/yyyy HH:MM): ')
#
# meeting_duration = float(input('Please Enter Meeting Duration: '))
# user_date = datetime.strptime(current_date_time, "%d/%m/%Y %H:%M")
#
# end_time = user_date + timedelta(hours=meeting_duration)
#
# print(f'The Start Date and Time of the meeting: {user_date}')
# print(f'The End Date and Time of the meeting: {end_time}')

# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current
# timezone, and then convert and print the date and time in another timezone of their choice.


# current_date_time = input('Please enter current date and time in a (dd/mm/yyyy HH:MM): ')
# user_date = datetime.strptime(current_date_time, "%d/%m/%Y %H:%M")
# user_input = input('Please Enter Time Zone you want to find out: ')
#
# if user_input == 'us':
#     time_in = user_date - timedelta(hours=7)
#     print(f'Currently at US : {time_in}')
# elif user_input == 'Brazil':
#     time_in = user_date - timedelta(hours=8)
#     print(f'Currently at Brazil: {time_in}')
# elif user_input == 'Russia':
#     time_in = user_date - timedelta(hours=2)
#     print(f'Currently at Brazil: {time_in}')
# elif user_input == 'Russia':
#     time_in = user_date + timedelta(hours=3)
#     print(f'Currently at Brazil: {time_in}')
# else:
#     print('Please Print Valid time zones ')


# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address,
# and check if it follows a valid email format.

# user_input = input('Please Enter your email: example@gmail.com: ')
# pattern = r'\d+|\w+@\w+\.\w+$'
# if re.match(pattern, user_input):
#     print(f'Your email {user_input} validate')
# else:
#     print('Please Enter Valid email')


# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a
# standard format. For example, convert "1234567890" to "(123) 456-7890"

# user_input = input('Please Enter you phone number: ')
# formatted = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', user_input)
# print(formatted)

# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if
# it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter,
# and one digit).

# user_password = input('Please Enter your Password to chek if it is strength enough: ')
# strength_password = r'([a-zA-Z]+\d)|(\d+[a-zA-Z])'
# if re.match(strength_password, user_password):
#         print('Your password is Strong')
# else:
#         print('Your password is not strong enough')


# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to
# input a word, and then search for and print all occurrences of that word in a sample text.

# user_input = input('Please Enter a word: ')
# make_list = re.findall(r'\w+', user_input)
# str1 = ''
# count = 0
# lst = []
# for i in make_list:
#     new_list = re.findall(i, user_input)
#     if len(new_list) > 1:
#         lst.append(i)
#     else:
#         pass
#
# print(lst)


# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text,
# and then identify and print all the dates present in the text

text = input('Please Enter a word with dates: ')

date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19[7-9][0-9]|20[0-4][0-9]|2050)$)'

dates = re.findall(date_pattern, text)

# Combine matched groups into full date strings
full_dates = [f"{day}/{month}/{year}" for day, month, year in dates]

# Print results
if full_dates:
    print("Dates found:")
    for d in full_dates:
        print(d)
else:
    print("No valid dates found in the text.")




