
# Python Dictionary and Set Exercises


# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
dict1 = {
    'n1': 2,
    'n2': 4,
    'n3': 0,
    'n4': 1,
    'n5': 5,
    'n6': 9,
}
print(sorted(dict1.values()))
print(sorted(dict1.values(), reverse=True))

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

dict2 = {'a': 1, 'b': 2}

dict2.update({'c': 3, 'd':5})
print(dict2)
#
# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print(new_dic)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

square_dict = {i: i**2 for i in range(1, 6)}
print(square_dict)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between
# 1 and 15 (both included) and the values are the square of the keys.
square_dict1 = {i: i**2 for i in range(1, 16)}
print(square_dict1)


# Set Exercises
# 1. Create a Set
# Write a Python program to create a set.

new_set = {'apple', 2, 'potato'}
print(new_set)

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

new_set = {'apple', 2, 'potato'}
for i in new_set:
    print(i)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

members = {'john', 'alex', 'Diana'}
members.add('apple')
print(members)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
members = {'john', 'alex', 'Diana', 'Eric', 'Zevi'}
members.pop()
members.remove('john')
members.discard('alex')
print(members)


# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

members = {'john', 'alex', 'Diana', 'Eric', 'Zevi'}
members.remove('john')
print(members)