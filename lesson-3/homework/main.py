#
# Homework: List and Tuple Exercises


# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

# lst1 = ['apples', 'grapes', 'orange', 'strawberry', 'blueberry']
# print(lst1[2])
#
# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
# lst1 = [1, 3, 4, 6, 7]
# lst2 = [4, 7, 9, 2, 0]
# res = lst1 + lst2
# print(res)
#
# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

# lst2 = [1, 4, 6, 5, 9, 3, 0, 7, 2, 8]
# new_lst = []
# last = len(lst2) - 1
# mid = int(len(lst2)/2)
# new_lst.append(lst2[0])
# new_lst.append(lst2[mid])
# new_lst.append(lst2[last])
# print(new_lst)

#
# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

# movies_lst = ['Hobbit', 'Seven', 'Inception', 'intuition']
# movies_tuple = tuple(movies_lst)
# print(movies_tuple)


# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
# city_lst = ['London', 'Moscow', 'Tashkent', 'Paris']
# if 'Paris' in city_lst:
#     print(f'Yes there is Paris in the list: {city_lst}')
# else:
#     print('No there is no City Paris in the List', city_lst)
#
# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

# num_lst = [1, 4, 7, 9, 3, 6, 0]
# dup = num_lst
# print(num_lst)
# print(dup)
#
# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
# num_lst = [1, 4, 7, 9, 3, 6, 0]
# new_lst = []
# new_lst.append(num_lst[len(num_lst)-1])
# for i in range(1, len(num_lst)-1):
#     new_lst.append(num_lst[i])
# new_lst.append(num_lst[0])
# print(new_lst)



# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
# lst_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(lst_tuple[3:7])


# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

# colors = ["red", "blue", "green", "blue", "yellow", "purple", "blue", "orange", "pink", "brown"]
# count = 0
# for i in colors:
#     if i == 'blue':
#         count += 1
#     else:
#         pass
# print(count, 'Blue colors in the list')

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

# animals = ("tiger", "elephant", "giraffe", "zebra", "lion", "monkey", "panda", "kangaroo", "wolf", "dolphin")
# print(animals.index('lion'))


# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
# tuple1 = (1, 4, 6, 8)
# tuple2 = (3, 5, 7, 9)
# merged = tuple1 + tuple2
# print(merged)

#
# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

# animals = ("lion", "giraffe", "zebra", "monkey", "panda", "kangaroo", "wolf", "dolphin")
# colors = ["red", "blue", "green", "blue", "yellow", "purple", "blue", "orange", "pink", "brown"]
# print('List length', len(colors))
# print('Tuple length', len(animals))


# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

# tup_num = (1, 5, 7, 8, 3)
# lst1 = list(tup_num)
# print(lst1)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
#
# num_tuple = (23, 87, 45, 12, 99, 56, 78, 34, 67, 10)
# max_num = 0
# min_num = 0
#
# for i in num_tuple:
#     if max_num < i:
#         max_num = i
#     else:
#         min_num = i
# print('Max Number in the Tuple is: ', max_num)
# print('Min Number in the Tuple is: ', min_num)

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
# words = ("apple", "banana", "chocolate", "elephant", "guitar", "ocean", "puzzle", "sunshine", "tiger", "whisper")
#
# print(words[::-1])

# Write a Python script to concatenate the following dictionaries to create a new one.




