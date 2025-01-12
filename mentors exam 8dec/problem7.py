# def all_primes (a,b):
#     ls = []
#     for i in range(a,b):
#         for j in range(2,i+1):
#             if i % j == 0 and j == i:
#                 ls.append(i)
#     return ls
# print(all_primes(10, 20))

#--^^^testing------------


def is_prime(n):
    for i in range(2, n+1):
        if n %i == 0 and i != n: #in number was devided by i and i was not the number that means n can't be prime since it got devided by a number that is not it self, so i return False 
            return False
    return True #if nothing that means it is prime and return true 
def range_of_primes(a,b):
    ls = [] # create a list to add prime numbers
    for i in range(a, b): #iterate over the range of numbers
        if is_prime(i): #check using the is_prime function
            ls.append(i)
    return ls#return primes 
print(range_of_primes(10,20))