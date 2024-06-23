from itertools import groupby

def sum_consecutives(arr):
    return [sum(group) for _, group in groupby(arr)]
#groupby(arr) groups same consecutive numbers 
#we go over on grups we created 
# _ is a key (ignored)
# group is what we use to go ower ur grupes
# sum (group) is used to calculate sum 
# gobroni tistlauri