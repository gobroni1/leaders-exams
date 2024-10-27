# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

def pal (n):
    n = n.replace(" ", "").lower()
    return n == n[::-1]
print(pal("A man a plan a canal Panama"))