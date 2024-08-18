#tuples in python


# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
# Tuples can also contain mixed data types
mixed_tuple = (1, "apple", 3.5)
print(mixed_tuple)  # Output: (1, 'apple', 3.5)
#

# Accessing Tuple Elements
# Accessing elements by index
first_element = my_tuple[0]
print(first_element)  # Output: 1
# Accessing elements from the end
last_element = my_tuple[-1]
print(last_element)  # Output: 3
#

# Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement.
# Unpacking a tuple
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3
# You can also unpack part of a tuple
a, *rest = my_tuple
print(a)  # Output: 1
print(rest)  # Output: [2, 3]
#

# Tuples can contain other tuples, leading to nested structures.
# Creating a nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5, 6))
# Accessing elements in a nested tuple
print(nested_tuple[1][1])  # Output: 3
#  

# You can count the occurrences of an element or find its index in a tuple.
# Counting occurrences
count = my_tuple.count(2)
print(count)  # Output: 1
# Finding the index of an element
index = my_tuple.index(3)
print(index)  # Output: 2


#
# practice 
#

tuple1 = (1, 2, 3, 5, 35, 33, 34, 66, 90)
list1 = []

# Loop to check for even numbers
for i in tuple1:
    if i % 2 == 0:
        list1.append(i)

# Check if the list is empty and convert it to a tuple
if len(list1) == 0:
    result = ()
else:
    result = tuple(list1)

print(result)  # Output: (2, 34, 66, 90) if list1 is not empty, otherwise ()
