# letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# marks = "!,@#$%^&*()_-+=<>,.?/|"

# #abc 2 cde
# #hello = mjppt with 5
# n = 5

# txt = "Hello! World"
# # print(letters[letters.index(txt[-1])+n])

# #--^^^^^thinking---------------
# ls = []
# temp = []
# words=txt.split(" ")
# for word in words:
#     for i in word:
#         if i in marks:
#             temp.append(i)
#         elif i.upper() == i:
#             temp.append((letters[letters.index(i.lower())+n]).upper())
#         else:
#             temp.append(letters[letters.index(i)+n])
        
#     ls.append("".join(temp))
#     temp = []
# print(" ".join(ls))


def encrypt (txt,n):
    letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    marks = "!,@#$%^&*()_-+=<>,.?/|1234567890"
    
    ls = []
    temp = []
    words=txt.split(" ")
    for word in words:
        for i in word:
            if i in marks:
                temp.append(i)
            elif i.upper() == i:
                temp.append((letters[letters.index(i.lower())+n]).upper())
            else:
                temp.append(letters[letters.index(i)+n])
            
        ls.append("".join(temp))
        temp = []
    return " ".join(ls)

print(encrypt("Hello, World!", 5))
print(encrypt("abc",2))
print(encrypt("xyz",3))
print(encrypt("Python", 0))
print(encrypt("abc", -1))


#ამას ქართულად ავხსნი თორემ წლებს წაიღებს ინგლისურად 

#პირველ რიგში ვქმნით ანბანს და მერე კიდევ სიმბოლოებს, რომ არ აგვირიოს კოდი, შემდეგ ტექსტს რომელსაც ვიღებთ ვანაწილებ სიტყვებად და ვინახავ სიაში. ორი for loop ის გამოყენებით იტერაციას ცახდენ თითოეული სიტყვის თითოეულ ასოზე თუ სიტყვის ასო დიდია მაშინ მის შესაბამის ასოს ვამატებ .upper() ით, თუ სიმბოლოა მაშინ პირდაპირ ვამატებ. რომელი ასო დავამატო ითვქლება ასე, გიღებს i-ს ანუ კონკტერულ ასოს და ვითვლი მერამდენეა .index(value) ის გამოყენებით, შემდეგ ამას ვამატებ n-ს და ვიღებ shifted ასოს, შემდეგ ამათ ვამატემ temp სიაშია (ანუ დროებითი) რომ ყველა სიტყვა ცალკე გავშიფრო და მერე დავამატო მთავარ სიაში.