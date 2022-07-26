#https://www.acmicpc.net/problem/1018
#M * N 체스판을 잘라서 칠한뒤, 8 * 8 체스판이 되어야한다.

#예상 방법
#1 dict구성해서 칠해진 칸의 개수를 센 뒤, 다시 더할 때 갯수를 세본다.
#2 w = 1,2  b = 3,4 로 구성해서 구해본다.
#3 칠한뒤, 칠한 칸을 0과 1로 구성해서, 갯수를 세어본다.

#결론
#1. 2차원 배열로 입력을 받는다.
#2. 진짜 체스판을 만든다.
#3. 틀린 부분에 1을 적는 2차원리스트를, 'w' 'b' 케이스 별로 2개 저장한다.
#4. 8개로 나누어서 모든 칸을 더해본다.

#입력받기
M, N = map(int, input().split())

#체스판 문자열로 입력받기
board = []
for m in range(M):
    board += [input()]
#print(board)

#진짜 체스판 만들기
real_board = [[0 for _ in range(N)]for _ in range(M)]
for m in range(M):
    for n in range(N):
        if m % 2 == 0: #y가 다를 경우 다르게 시작하는 것을 고려
            if n % 2 == 0:
                real_board[m][n] = 'W'
            else:
                real_board[m][n] = 'B'
        else:
            if n % 2 == 0:
                real_board[m][n] = 'B'
            else:
                real_board[m][n] = 'W'
#print(real_board)

#체스판 칠할 칸 만들어서 칠하기
check_A = [[0 for _ in range(N)]for _ in range(M)] #맨앞이 W
check_B = [[0 for _ in range(N)]for _ in range(M)] #맨앞이 B

for m in range(M):
    for n in range(N):
        if board[m][n] != real_board[m][n]:
            check_A[m][n] = 1
        else:
            check_B[m][n] = 1

#print(check_A)
#print(check_B)
#체크보드 판별하기
summyA = 0
summyB = 0
save = -1
for y in range(M - 8 + 1):
    for x in range(N - 8 + 1):
        for m in range(8):
            for n in range(8):
                summyA += check_A[m+y][n+x]
                summyB += check_B[m+y][n+x]
        if save == -1:
            save = min([summyA, summyB])
        else:
            save = min([summyA, summyB, save])
        summyA = 0
        summyB = 0

print(save)
    
            