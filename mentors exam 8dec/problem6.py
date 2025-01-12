def chek_sudoku (board):
    if not all(board[row][col] != "0" for row in range(9) for col in range(9)):  #see if the board is full or not 
        return False
    
    for row in board:
        if not check_sudoku2(row):  #wery simple just iterate over rows 
            return False
            
    for col in range(9):
        column = [board[row][col] for row in range(9)]   #iterating over list (beacause every row is a list) with spesific index (so you get every x index from every list giving you a row)
        if not check_sudoku2(column):
            return False
        
    for row in range (0,9,3):
        for col in range(0,9,3):#this for loops are for 3 by 3 grids 
            by_3 = []
            for i in range(3):
                for j in range(3):
                    by_3.append(board[row+i][col + j])
            if not check_sudoku2(by_3):              #by getting 3 by 3 grid numbers and passing them to dupes function we finde if there is any dupes in 3 by 3 areas 
                return False
    return True
        
def check_sudoku2 (n):
    return len(n) == len(set(n)) #this check for dupes using sets because they automaticly delete duplicats 


print(chek_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 9, 7, 9]]))