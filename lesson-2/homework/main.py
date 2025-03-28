import random


# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

# user_name = input('Please enter your Name: ')
# birth_year = int(input('Please enter you Birth Year: '))
#
# age = 2025 - birth_year
#
# print(f'{user_name} your AGE is {age}')


# 2. Extract Car Names
# Extract car names from the following text:

# txt = 'LMaasleitbtui'
#
# print(txt[::2])
# print(txt[1::2])

# 3. . Extract Car Names
# Extract car names from the following text:

# txt = 'MsaatmiazD'
#
# print(txt[::2])
# print(txt[::-2]) # Counting from the end of a string


# 4. Extract Residence Area
# Extract the residence area from the following text:

# txt = "I'am John. I am from London"

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

# user_name1 = input('Please enter your name: ')
#
# reverse_name = user_name1[::-1]
# print(reverse_name)


# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

# str1 = input('Please enter a word to count its VOWELS: ')
# count = 0
# for i in str1.lower():
#
#     if i == 'a' or i == 'y' or i == 'i' or i == 'o' or i == 'e' or i == 'u':
#         count += 1
#     else:
#         pass
#
# print(f'The number of Vowels in the sentence: {count}')

#
# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value

# num = input('Please enter numbers with comas: ')
# new_ls = num.split(',')
# max_num = 0
# for i in range(0, len(new_ls)-1):
#     if max_num < int(new_ls[i]):
#         max_num = int(new_ls[i])
#     else:
#         pass
# print(max_num)


# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

# pol = input('Please enter a word to check weather it is Palindrome or not: ')
# if pol[::-1].lower() == pol.lower():
#     print(f'The word {pol} is a Palindrome: {pol[::-1]}')
# else:
#     print(f'The word {pol} is not Palindrome: {pol[::-1]} ')


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.


# email = input('Please enter your email: ')
# try:
#     email_domain = email.split('@')
#     print(email_domain[1])
# except:
#     print('Please enter right format of email: example@email.com')


# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.


