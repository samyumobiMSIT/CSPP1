"""
{ item_description }
"""
def print_sudoku(grd):
    for i in range(9):
        print(grd[i])
        print('Given sudoku is solved')
"""
creating a set
"""
def create_set(a, row, col):
    li_st = set()
    for i in range(9):
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
            s = set()
            if a[i][j] == '0':
                s = create_set(a, i, j)
            if len(s) != 0:
                for p in "123456789":
                    if p not in s:
                        result += p
                print(result)

if __name__ == "__main__":
    grid = [['0' for x in range(9)]for y in range(9)]
    INP_UT = input()
    k = 0
    for i in range(9):
        for j in range(9):
            if INP_UT[k] != '.':
                grid[i][j] = INP_UT[k]
            k += 1
    possiblechoice(grid)

