import sys
sys.stdin = open('input.txt')
#총 경우의 수 5! 전부 계산해보고 가지치자
count = 0
def dfs(n, N, top, sum_r):
    global count
    print(sum_r)
    if n == 5: # 다 도착했을때
        print(dfs_arr, ' ', sum_r, ' ', top_arr)
        count += 1
        return
    else:
        for idx in range(N):
            if ch_li[idx] == 0:
                ch_li[idx] = 1 #체크리스트에 넣어주고
                dfs_arr[n] = idx #n번째를 idx로 만든다.
                if n == 0: #시작일 경우 6가지 종류로 세팅한다.
                    for dice in range(6):
                        top_arr[n] = arr[idx][top_bo(dice)]
                        sum_r += side(dice, arr[idx])
                        dfs(n+1, N, arr[idx][dice], sum_r)
                        sum_r -= side(dice, arr[idx])
                else:
                    #print(arr[n], top)
                    top_idx = arr[idx].index(top)
                    top_arr[n] = arr[idx][top_idx]
                    sum_r += side(top_idx, arr[idx])
                    dfs(n+1, N, arr[idx][top_bo(top_idx)], sum_r)
                    sum_r -= side(top_idx, arr[idx])
                ch_li[idx] = 0
def top_bo(t): #인덱스를 넣으면 반대위치를 표출
    if t == 0: return 5
    if t == 5: return 0
    if t == 1: return 3
    if t == 3: return 1
    if t == 2: return 4
    if t == 4: return 2
def side(t, li): #인덱스를 넣으면 맥스값을 표출
    if t == 0: return max(li[1],li[2],li[3],li[4])
    if t == 5: return max(li[1],li[2],li[3],li[4])
    if t == 1: return max(li[0],li[2],li[5],li[4])
    if t == 3: return max(li[0],li[2],li[5],li[4])
    if t == 2: return max(li[1],li[0],li[3],li[5])
    if t == 4: return max(li[1],li[0],li[3],li[5])
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
ch_li = [0] * N
dfs_arr = [0] * N
top_arr = [0] * N
dfs(0, N, 0, 0)
print(count)
