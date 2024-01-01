# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split())
# BOARD = [list(input()) for _ in range(R)]
# # visited = [[0 for _ in range(C)] for _ in range(R)]


# def loop(r, c, cnt):
#     global answer
#     answer = max(cnt, answer)
#     # print(checked)

#     for gr, gc in ((r+1, c),(r-1, c),(r, c+1),(r, c-1)):
#         if 0 <= gr < R and 0 <= gc < C and BOARD[gr][gc] not in checked:
#             checked.add(BOARD[gr][gc])
#             loop(gr, gc, cnt+1)
#             checked.remove(BOARD[gr][gc])

# answer = 1
# checked = set()
# checked.add(BOARD[0][0])
# loop(0, 0, 1)
# print(answer)

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny])
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)

# 시간 왤케 촉박하냐 이정도면 쓰레기 문제 아니니냐냐냐!