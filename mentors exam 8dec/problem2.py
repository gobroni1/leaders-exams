# text = "lets test this for second time time time should be ten words"

# words = text.lower().split(" ")

# ls = []

# for word in words:
#     if word not in ls:
#         ls.append(word)
# print(len(ls))

#----^^^^^^^^thinking----------------------------------

def uqique_count (text):
    #make sure words are lower case and split them so we can itarate 
    words = text.lower().split(" ")
    #create a list to add unique words
    ls =[]
    #since every word is in the list we can itarate and add only words that are not allready in the ls, so if word we added comes again we will not add it 
    for word in words:
        if word not in ls and word != "": #this is done becase in some cases if extra space was in the sentanse it woould count it as a word
            ls.append(word)
    return len(ls)

print(uqique_count("The quick brown fox jumps over the lazy dog"))
print(uqique_count("Hello hello world!"))
print(uqique_count(""))
print(uqique_count("Python is fun. Python is cool"))
print(uqique_count("one word"))