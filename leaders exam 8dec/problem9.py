def is_prime(n):
    for i in range(2, n+1):
        if n %i == 0 and i != n: #in number was devided by i and i was not the number that means n can't be prime since it got devided by a number that is not it self, so i return False 
            return False
    return True #if nothing that means it is prime and return true 


# this is same as one from mornings exam

def prob9 (start, end): 
    ls = []           #create list to add all numbers 
    ls1 = []          #creat list to add non prime numbers
    for i in range(start, end+1): #+1 to include end number
        ls.append(i) #add numbers to ls
    for i in ls:
        if is_prime(i) == False: #filter prime nimbers using function from mentores exam
            ls1.append(i)
    return ls1            
  
print(prob9(10, 20))
print(prob9(1, 10))
print(prob9(20, 30))
print(prob9(24,25))