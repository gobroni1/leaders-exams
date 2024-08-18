# dictionarys in python

# Creating a dictionary with key-value pairs
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print(student_scores)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
#

# Accessing a value by key
alice_score = student_scores["Alice"]
print(alice_score)  # Output: 85
#

# Adding a new key-value pair
student_scores["David"] = 88
# Modifying an existing value
student_scores["Alice"] = 90
print(student_scores)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88}
#

# Using del to remove a key-value pair
del student_scores["Charlie"]
# Using pop to remove a key-value pair and return its value
bob_score = student_scores.pop("Bob")
print(student_scores)  # Output: {'Alice': 90, 'David': 88}
print(bob_score)       # Output: 92
#

# Iterating over keys
for key in student_scores:
    print(key, student_scores[key])
# Iterating over key-value pairs
for key, value in student_scores.items():
    print(f"{key}: {value}")
#

#
# practise 
#

ipt_city = input("choose a country and get capital")
cap_city = {"france":"paris",}
capital =cap_city.get(ipt_city, "f u")
print(cap_city[capital]) 