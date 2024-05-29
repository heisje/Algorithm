import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())

grid = [list(input()) for _ in range(M)]
requests = [list(map(int, input().split())) for _ in range(K)]

cSum = {
    'J':[[0 for _ in range(N+1)] for _ in range(M+1)],
    'I':[[0 for _ in range(N+1)] for _ in range(M+1)],
    'O':[[0 for _ in range(N+1)] for _ in range(M+1)]
}


for m in range(1,M+1):
    for n in range(1,N+1):
        cSum['J'][m][n] = cSum['J'][m-1][n] + cSum['J'][m][n-1] - cSum['J'][m-1][n-1]
        cSum['I'][m][n] = cSum['I'][m-1][n] + cSum['I'][m][n-1] - cSum['I'][m-1][n-1]
        cSum['O'][m][n] = cSum['O'][m-1][n] + cSum['O'][m][n-1] - cSum['O'][m-1][n-1]

        cSum[grid[m-1][n-1]][m][n] += 1

for a,b,c,d in requests:
    answer = {
        'J':0,
        'I':0,
        'O':0
    }

    for t in ['J', 'I', 'O']: 
        answer[t] = cSum[t][c][d] - cSum[t][a-1][d] - cSum[t][c][b-1] + cSum[t][a-1][b-1]
    
    print(f"{answer['J']} {answer['O']} {answer['I']}")

