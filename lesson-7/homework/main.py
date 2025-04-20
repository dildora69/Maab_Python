# 1.is_prime(n) funksiyasi

# num = int(input('Please enter a number to check if it is a prime or not: '))
#
#
# def is_prime(n):
#     if n <= 0:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return f'The number {n} is a PRIME number'
#
#
# print(is_prime(num))


# 2. digit_sum(k) funksiyasi

# num = input('Please enter a number to sum up its digits: ')
#
#
# def digit_sum(k):
#     sum = 0
#     for i in k:
#         sum += int(i)
#     return sum
#
# print(digit_sum(num))


# 3. Ikki sonning darajalari

# n = int(input('Please enter a number: '))
# res = 1
# for i in range(1, n+1):
#     res = 2 ** i
#     if res <= n:
#         print(res)