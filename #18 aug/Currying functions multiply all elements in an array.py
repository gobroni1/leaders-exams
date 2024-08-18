def multiply_all (arr):
    def mult (n):
        return [x * n for x in arr]
    return mult