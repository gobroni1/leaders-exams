# [expression for item in iterable] #

# list compherisons in python

# Creating a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 
 
# Creating a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
#

# Creating a 3x3 matrix using nested list comprehensions
matrix = [[x + y for x in range(3)] for y in range(3)]
print(matrix)  # Output: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
#
 
# Converting a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
#

# Creating pairs of numbers from two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
#


#
# practice
#

or_list = ["hello", "giorgi", "some numbers", "ho", "g", "hello", ""]
new_list = [x for x in or_list if len(x) > 2]
print(new_list)