def print_grid(grd):
    for i in range(9):
        print(grd[i])
def create_set(a, row, col):
    li_st = set()
    for i in range(9):
        if a[row][i] != '0':
            li_st.add(a[row][i])
        if a[i][col] != '0':
            li_st.add(a[i][col])
    return li_st

def possiblechoice(a):
    for i in range(9):
        for j in range(9):
            result = ""
            s = set()
            if a[i][j] == '0':
                s = create_set(a, i, j)
                # print(s)
            if len(s) != 0:
                for eaca in "123456789":
                    if eaca not in s:
                        result += eaca
                print(result)

if __name__ == "__main__":
    grid = [['0' for x in range(9)]for y in range(9)]
    inp_ut = input()
    k = 0
    for i in range(9):
        for j in range(9):
            if inp_ut[k] != '.':
                grid[i][j] = inp_ut[k]
            k += 1
    possiblechoice(grid)

