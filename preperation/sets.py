#1 sets in python 

# they do not have defined order, they only contain distingt elements, buplicats are automatically removed. you can add or remove items.

# Creating a set with some numbers
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
# 

# Adding an element to a set
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
#

# Removing an element from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}
# Using discard to remove an element (no error if the element doesn't exist)
my_set.discard(10)  # No error, even though 10 is not in the set
#

# Two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union of sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
#

# Checking if an element is in the set
print(2 in my_set)  # Output: True
print(10 in my_set)  # Output: False


#
# practice 
#

ipt_set1 = input("enter random numbers: ")
ipt_set2 = input("enter random numbers: " )

print("duplicats will be removed!")

set1 = set()
set2 = set()

for i in ipt_set1:
    set1.add(int(i))
for i in ipt_set2:
    set2.add(int(i))
print(set1.intersection(set2), set1.union(set2), set1.difference(set2))

num = input("finde out if number is in the set")
print(f"{num} in set1 is {num in set1}")
print(f"{num} in set2 is {num in set2}")