def binggo_checker(board):
    cnt = {
        'O':0,
        'X':0,
        '.':0
    }
    bing_cnt = {
        'O':0,
        'X':0
    }
    for n in range(3):
        for m in range(3):
            cnt[board[n][m]] += 1
        if board[n][0] != '.' and board[n][0] == board[n][1] == board[n][2]:
            bing_cnt[board[n][0]] += 1
        if board[0][n] != '.' and board[0][n] == board[1][n] == board[2][n]:
            bing_cnt[board[0][n]] += 1
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        bing_cnt[board[0][0]] += 1
    if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
        bing_cnt[board[0][2]] += 1
    
    return (cnt['O'], cnt['X'], bing_cnt['O'], bing_cnt['X'])

def solution(board):
    
    o_cnt, x_cnt, o_binggo, x_binggo = binggo_checker(board)
    if o_cnt < x_cnt:
        return 0
    if o_cnt >= x_cnt + 2:
        return 0
    if o_binggo > 0 and x_binggo > 0:
        return 0
    if o_binggo > 0 and o_cnt == x_cnt:
        return 0
    if x_binggo > 0 and o_cnt > x_cnt:
        return 0
    
    return 1