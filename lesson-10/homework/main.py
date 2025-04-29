
import re

# m = 'sldksldsf'
# a = 'a'
# print(re.match('[^abc]', m))
# print(re.match('[abc]', a))
# print(re.match('[abc]+', a))  # '+' operand means 1 and more  and '*' means 0, 1 and more
#
# print(re.match('.*', m))  # '.' - means is equal only 1 char and '*' - means match everything in the giving string

# name = 'Dalia'
# print(re.match('^D.*', name)) # '^' - means that D is the first char in the name string
# print(re.match('.*a$', name)) # '$' -  is the last char


number = '995694518'
print(re.match('\d*', number))
print(re.match('\d{2}\d{3}\d{2}\d{2}', number))


email = 'test123@gmail.com'
pattern = "^[\w\.-]+@[\w\.-]+\.\w+$"
print(re.match(pattern, email))
