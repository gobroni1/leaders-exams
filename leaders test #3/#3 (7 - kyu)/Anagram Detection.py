def is_anagram(test, original):
    str1 = sorted(test.lower())
    or_str = sorted(original.lower())
    if str1 == or_str:
        return True
    else:
        return False
#gobroni
