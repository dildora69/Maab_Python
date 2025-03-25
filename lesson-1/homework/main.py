# Homework:
#
# Given a side of square. Find its perimeter and area.

a = int(input('Please enter the a side of a square:  '))

perimeter = 2 * a
area = a ** 2

print(f'Perimeter of a Square:  {perimeter}')
print(f'Area of a Square: {area}')

# Given diameter of circle. Find its length.

d = int(input('Please enter a diameter of a circle to find its LENGTH:  '))
length = 3.14 * d

print(f'Length of a Square: {length} ')

# Given two numbers a and b. Find their mean.

print('This program is to calculate the mean of GIVEN TWO NUMBERS A and B')
a = int(input('Please enter a number for A: '))
b = int(input('Please enter a number for B: '))
mean = (a + b)/2

print(f'Mean: {mean}')

# Given two numbers a and b. Find their sum, product and square of each number.

print('This program is to calculate the sum, product and square of each GIVEN TWO NUMBERS A and B')
a = int(input('Please enter a number for A: '))
b = int(input('Please enter a number for B: '))

sum = a + b
product = a * b
sqrA = a**2
sqrB = b**2

print(f'''
Sum: {sum}
Product: {product}
Square of A: {sqrA}
Square of B: {sqrB}
''')
