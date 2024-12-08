def is_prime(n):
    for i in range(2, n+1):
        if n %i == 0 and i != n: #in number was devided by i and i was not the number that means n can't be prime since it got devided by a number that is not it self, so i return False 
            return False
    return True #if nothing that means it is prime and return true 


def sq (n):
    ls = []
    sum =1 #default is one because if it was 0 it would return 0 becasee 0 * x is 0
    for i in range(2,n+1):
        if is_prime(i):    #borrow function from previos problen and chek for primes 
            ls.append(i)
    for j in ls: #itarate and * all 
        print(j)
        sum = sum * j
    return sum
print(sq(5))      
print(sq(10))
print(sq(1))
print(sq(7))
print(sq(11))
    