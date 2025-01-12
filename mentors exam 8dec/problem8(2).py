def xbonacci (n, x):
    #თვიდან იქნება N ის მნიშვნელობით 
    result = x[:]
    #იტერაცია მოხდება x ის სიგრძიდან n მდე და  
    for i in range(len(x),n):
        result.append(sum(result[i - len(x):i])) #ნუ ეს მარტივია, უბრალოდ ვამატებთ წინა ციფრებს შემდეგებს და ეგაა
    return result

print(xbonacci([1,1,2], 10))