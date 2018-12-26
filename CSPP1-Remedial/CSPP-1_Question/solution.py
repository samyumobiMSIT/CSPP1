"""
{ Solution }
"""
def print_sudoku(grd):
    for i in range(9):
        print(grd[i])
        #if sudoku is completely filled with dots.
        print('Given sudoku is solved')
        #not checking if length is 81
"""
creating a set
"""
def create_set(a, row, col):
    #set to removve duplicates
    li_st = set()
    for i in range(9):
        #checks if row or col is != 0 and adds elements to list
        if a[row][i] != '0':
            li_st.add(a[row][i])
        if a[i][col] != '0':
            li_st.add(a[i][col])
    return li_st
"""
possibilities
"""
def possiblechoice(a):
    for i in range(9):
        for j in range(9):
            result = ""
            # taking set to eliminate duplicate values
            s = set()
            if a[i][j] == '0':
                s = create_set(a, i, j)
            if len(s) != 0:
                for p in "123456789":
                    if p not in s:
                        #if number is not present in the game pseudocide. then it will add the number
                        result += p
                print(result)

if __name__ == "__main__":
    # x-row, y-col intially everything is 0, 9*9=81
    grid = [['0' for x in range(9)]for y in range(9)]
    INP_UT = input() 
    #taking testcases input in input
    k = 0
    for i in range(9):
        for j in range(9):
            # if input not = to .
            if INP_UT[k] != '.':
                #store value in grid
                grid[i][j] = INP_UT[k]
                #incrementing k
            k += 1
    #checking possible choices in the grid
    possiblechoice(grid)

