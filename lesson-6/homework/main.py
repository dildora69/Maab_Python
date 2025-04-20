
# 1. Modify String with Underscores


# def insert_shifted_underscores(txt):
#     vowels = "aeiouAEIOU"
#     i = 3  # Start at index 3 (4th character), since we add after every 3 characters
#     result = list(txt)  # Convert to list to make insertion easy
#
#     while i < len(result):
#         # Shift if vowel or underscore is at or after position i
#         if result[i - 1] in vowels or (i < len(result) and result[i] == '_'):
#             i += 1  # shift the underscore to the next character
#             if i >= len(result):  # don’t add underscore at the end
#                 break
#         result.insert(i, '_')  # insert underscore
#         i += 4  # skip next 3 characters after underscore
#
#     return ''.join(result)
#
# # Test
# txt = "haelloxyzabcde"
# print(insert_shifted_underscores(txt))




# 2. Integer Squares Exercise

# n = int(input('Please enter an Integer: '))
#
# squares = (i**2 for i in range(0, n))
# for square in squares:
#     print(square)



# 3. Loop-Based Exercises

# n = int(input('Please enter an Integer: '))
#
# # ex-1
# i = 0
# while n >= 0:
#     print(i)
#     i += 1
#     n-=1

# ex -2
# i = 1
#
# while i <= n:
#     for j in range(1, i+1):
#         print(j, end=' ')
#     i += 1
#     print('')

# Exercise 4: Print multiplication table of a given number

# n = int(input('Please enter an Integer: '))

# i = 1
# while i <= 10:
#     print(i*n)
#     i += 1


# Exercise 5: Display numbers from a list using a loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in range(1, 5):
#     print(numbers[i])


# Exercise 6: Count the total number of digits in a number

# n = input('Please enter an Integer: ')
# count = 0
# for i in range(1, len(n)+1):
#     count += 1
#
# print(f'The total number of digits in the number {n} is: {count}')


# Exercise 7: Print reverse number pattern

# n = int(input('Please enter an Integer: '))
#
#
# while n > 0:
#     for j in range(n, 0, -1):
#         print(j, end=' ')
#     n -= 1
#     print('')

# Exercise 8: Print list in reverse order using a loop

# list1 = [10, 20, 30, 40, 50]
#
# for i in range(len(list1)-1, -1, -1):
#     print(list1[i])


# Exercise 9: Display numbers from -10 to -1 using a for loop

# for i in range(-10, 0, 1):
#     print(i)


# Exercise 10: Display message “Done” after successful loop execution
# n = 5
# i = 0
# while n > 0:
#     print(i)
#     i += 1
#     n -= 1
# print('Done!')



# Exercise 11: Print all prime numbers within a range

# n = int(input('Please enter an Integer: '))
# if n >= 1:
#     for i in range(25, n+1):
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#         if is_prime:
#             print(i)


# Exercise 12: Display Fibonacci series up to 10 terms
# a, b = 0, 1
# for i in range(0, 10):
#     print(a, end=' ')
#     a, b = b, a+b


# Exercise 13: Find the factorial of a given number


# n = int(input('Please enter a number: '))
# res = 1
# for i in range(1, n+1):
#     res *= i
# print(res)


# 4. Return Uncommon Elements of Lists

# list1 = [1, 1, 2]
# list2 = [2, 3, 4]
# new_list = list1.extend(list2)
# print(new_list)
