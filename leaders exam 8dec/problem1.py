def pos_sum (ls):
    sum = 0#create varuable to add all
    for i in ls:
        if i > 0: #check if number is negative or not (we only need positives)
            sum += i
    return sum #return sum of all positives 

print(pos_sum([1, -4, 7, 12]))
print(pos_sum([-1, -2, -3, -4]))
print(pos_sum([]))



def pos_remastered (l2):
    return sum([i for i in l2 if i > 0])
print(pos_remastered([1,-4,7,12]))