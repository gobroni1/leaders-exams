# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"


def P_to_S (s):
    sn = ""
    for i in s:
        if i.isupper() and sn:
            sn +="_"
        sn += i.lower()
    return sn
print(P_to_S("TestController"))