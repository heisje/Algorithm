d_x = (0, 0, 1, -1)
d_y = (1, -1, 0, 0)


from collections import deque

def solution(m, n, board):
    answer = 0
    board = print(list(map(list, board)))
    visited = board[:]
    for y in range(m-1):
        for x in range(n-1):
            if board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1]:
                
                dq = deque()
                dq.append(visited[y][x])
    
    return answer

solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])