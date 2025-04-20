#
# Exception Handling Exercises
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
#
# try:
#     a = 5 / 0
# except ZeroDivisionError as z:
#     print('Sorry, But you can not divide a number by 0', z)


# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     n = int(input('Please enter an INTEGER NUMBER only: '))
# except ValueError as v:
#     print('Please Enter Only Integer number', v)



# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# try:
#     with open(file_name, 'r') as file:
#         content = file.read()
# except FileNotFoundError as f:
#     print('Sorry, But there is no such file', f)


# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    a = int(input('Please enter 1st Number: '))
    b = int(input('Please enter 2nd Number: '))
except TypeError as t:
    print('Please enter Two NUMBERs', t)

# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)

except PermissionError:
    print(f"Permission denied: You don't have permission to open '{file_name}'.")

# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    index = int(input("Enter the index of the element you want to access: "))
    print(f"Element at index {index} is {my_list[index]}")

except IndexError:
    print(f"IndexError: Index {index} is out of range. List has {len(my_list)} elements (0 to {len(my_list)-1}).")

# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    number = input("Please enter a number: ")
    number = float(number)  # Convert to number (supports int and float)
    print(f"You entered: {number}")

except KeyboardInterrupt:
    print("\nInput cancelled by user (KeyboardInterrupt).")



# File Input/Output Exercises
# Write a Python program to read an entire text file.
with open("file.txt") as f:
    print(f.read())
# Write a Python program to read first n lines of a file.
n = 3
with open("file.txt") as f:
    for _ in range(n):
        print(f.readline(), end='')

# Write a Python program to append text to a file and display the text.
with open("file.txt", "a+") as f:
    f.write("\nAppended line.")
    f.seek(0)
    print(f.read())

# Write a Python program to read last n lines of a file.
n = 2
with open("file.txt") as f:
    print(''.join(f.readlines()[-n:]))

# Write a Python program to read a file line by line and store it into a list.
with open("file.txt") as f:
    lines = f.readlines()

# Write a Python program to read a file line by line and store it into a variable.
with open("file.txt") as f:
    content = f.read()

# Write a Python program to read a file line by line and store it into an array.
with open("file.txt") as f:
    arr = [line.strip() for line in f]

# Write a Python program to find the longest words.
with open("file.txt") as f:
    print(max(f.read().split(), key=len))

# Write a Python program to count the number of lines in a text file.
with open("file.txt") as f:
    print(len(f.readlines()))

# Write a Python program to count the frequency of words in a file.
from collections import Counter
with open("file.txt") as f:
    print(Counter(f.read().split()))

# Write a Python program to get the file size of a plain file.
import os
print(os.path.getsize("file.txt"))

# Write a Python program to write a list to a file.
import os
print(os.path.getsize("file.txt"))

# Write a Python program to copy the contents of a file to another file.
data = ["one", "two", "three"]
with open("file.txt", "w") as f:
    f.write("\n".join(data))

# Write a Python program to combine each line from the first file with the corresponding line in the second file.
with open("file.txt") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

# Write a Python program to read a random line from a file.
with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

# Write a Python program to assess if a file is closed or not.
import random
with open("file.txt") as f:
    print(random.choice(f.readlines()))

# Write a Python program to remove newline characters from a file.
f = open("file.txt")
print(f.closed)  # False
f.close()
print(f.closed)  # True

# Write a Python program tat takes a text file as input and returns the number of words in a given text file.

with open("file.txt") as f:
    print(len(f.read().split()))
