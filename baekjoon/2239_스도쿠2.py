def check_number(r, c, num):
    if row[r][num] or column[c][num] or mini_square[r // 3 * 3 + c // 3][num]:
        return False
    else:
        return True

def update_number(r,c,num,tf):
    row[r][num] = tf
    column[c][num] = tf
    mini_square[r // 3 * 3 + c // 3][num] = tf

def backTracing(r,c):
    if c == 9:
        r += 1
        c = 0
    if r == 9:
        return True
    
    if sudoku[r][c] != 0:
        return backTracing(r,c+1)
    
    for num in range(1,10):
        if not check_number(r,c,num):
            continue

        update_number(r,c,num,True)
        sudoku[r][c] = num

        if backTracing(r,c+1):
            return True
        
        update_number(r,c,num,False)
        sudoku[r][c] = 0

    return False

str_sudoku = [list(input()) for _ in range(9)]
row = [[False] * 10 for _ in range(9)]
column = [[False] * 10 for _ in range(9)]
mini_square = [[False] * 10 for _ in range(9)]
sudoku = [[0 for _ in range(9)] for _ in range(9)]

for r in range(9):
    for c in range(9):
        k = int(str_sudoku[r][c])
        row[r][k] = True
        column[c][k] = True
        mini_square[r // 3 * 3 + c // 3][k] = True
        sudoku[r][c] = k

backTracing(0,0)

for r in range(9):
    st = ''
    for c in range(9):
        st += str(sudoku[r][c])
    print(st)