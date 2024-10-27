# 9) Prime time (4 ქულა)

# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]
def primes (n):
    prems = []
    for num in range (2,n+1):
        pe = True
        for i in range (2, int(num**0.5)+1):
            if num % i ==0:
                pe = False
                break
        if pe:
            prems.append(num)
    return prems
print(primes(11))