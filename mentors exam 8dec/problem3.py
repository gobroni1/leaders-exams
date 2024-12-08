# text = "hello world"

# words = text.split(" ")

# print(" ".join(words[::-1]))

#--^^^thinking-----

def reserve_word (s):
    if s == " " or "":
        return "" #if empty string is given return empty string
    
    words = s.split(" ") #put all word in a list 
    words2 = [] #create second list to filter " " - s from the first list
    for i in words: #filter
        if i != "":
            words2.append(i)
    return " ".join(words2[::-1]) #return the filtered list in revers. "::-1" is same as "start to finish from the end" 


print(reserve_word("python is great"))    
print(reserve_word("Hello World"))
print(reserve_word("a b c"))
print(reserve_word(""))
print(reserve_word(" spaces "))