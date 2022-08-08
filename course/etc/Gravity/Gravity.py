import sys
sys.stdin = open('input.txt')

#핵심 : 체크하는 value 값 뒤로부터 다른 값을 비교해서 다른 값이 더 작으면 낙차가 +1 된다.
N = int(input())
for testcase in range(N):
    length = int(input())

    grid = list(map(int, input().split())) #모든 리스트
    max_count = 0                          #최대낙차
    for i in range(len(grid)): #숫자의 개수 세기
        count = 0              #낙차
        for j in range(len(grid)): #i와 j를 비교하기 위해 2중 반복
            if j > i:
                if grid[i] > grid[j]: #i j 비교 후 카운터 세기
                    count += 1
            if count > max_count:     #최대값을 구한다.
                max_count = count
    print(f'#{testcase + 1} {max_count}')



