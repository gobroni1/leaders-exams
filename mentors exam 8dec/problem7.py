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
        if n %i == 0 and i != n:
            return False
    return True

ls = []
for i in range(10, 20):
    if is_prime(i):
        ls.append(i)
        
print(ls)