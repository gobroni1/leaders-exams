def anagram_check (s1, s2):
    #make sure all word are lower case and have no gaps
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    
    #we know anagra s should have same letters, so if we sort them whey should give us same strings since cba sorted is same as bac sorted
    return sorted(s1) == sorted(s2)


print(anagram_check("listen", "silent"))