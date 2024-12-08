# n = 3

#start with one 
#end with one 
#put sum in the middle 

# 1, 1.1 , 1.2.1 
def pascals_triangle(n):
    tr = []
    for i in range (n): #this for loop iterates ower rows in the triangle 
        rw = [1] * (i +1)
        
        for j in range(1, i):#this for loop iterates over each item in each row
            rw[j] = tr[i-1][j-1] +tr[i-1][j] #in here i-1 is last row (it is neded to calculate next item)|| tr[i-1][j-1] is left element and tr[i-1][j]is top one and rw[j] is set to sum of left and top 
        tr.append(rw)
    return tr

print(pascals_triangle(1))
print(pascals_triangle(2))
print(pascals_triangle(3))
print(pascals_triangle(5))


#this was hard bro!!!!!!