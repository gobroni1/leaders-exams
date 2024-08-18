# lambda arguments: expression


# adds 10 to a number 
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
#

# multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12
# 

# to map do for every iteratable in a list 
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
# 

# filter odds out 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter out even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]
