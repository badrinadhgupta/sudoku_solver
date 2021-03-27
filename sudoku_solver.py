s = [[5, 0, 0, 0, 1, 0, 0, 0, 4],
     [2, 7, 4, 0, 0, 0, 6, 0, 0],
     [0, 8, 0, 9, 0, 4, 0, 0, 0],
     [8, 1, 0, 4, 6, 0, 3, 0, 2],
     [0, 0, 2, 0, 3, 0, 1, 0, 0],
     [7, 0, 6, 0, 9, 1, 0, 5, 8],
     [0, 0, 0, 5, 0, 3, 0, 1, 0],
     [0, 0, 5, 0, 0, 0, 9, 2, 7],
     [1, 0, 0, 0, 2, 0, 0, 0, 3]]

index = [0, 0]

def printsudoku(arr):
    for i in range(0,9):
        print(arr[i])

def checkrow(arr, row, n):
    for i in range(0, 9):
        if arr[row][i] == n:
            return False
    return True

def checkcol(arr, col, n):
    for i in range(0, 9):
        if arr[i][col] == n:
            return False
    return True

def checkbox(arr,r,c,n):
    sr = r-r%3
    sc = c-c%3
    for i in range(3):
        for j in range(3):
            if arr[i+sr][j+sc]==n:
                return False
    return True

def checkzeros(arr,index):
    for row in range(0,9):
        for col in range(0,9):
            if arr[row][col]==0:
                index[0] = row
                index[1] = col
                return True
    return False

def solvesudoku(s):

    index = [0,0]
    if not checkzeros(s,index):
        return True

    row = index[0]
    col = index[1]

    for num in range(1,10):
        if checkrow(s,row,num) and checkcol(s,col,num) and checkbox(s,row,col,num):
            s[row][col] = num

            if(solvesudoku(s)):
                return True

            s[row][col] = 0

    return False

solvesudoku(s)
printsudoku(s)