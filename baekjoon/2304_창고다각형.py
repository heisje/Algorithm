# 핵심 : 가장 높은 건물 기준으로 계단식으로 올라갔다 내려온다. 건물 사이의 거리만큼을 곱해서 거리를 구한다.

# 방법 

#입력받기
N = int(input())
pillars = []
for n in range(N):
    pillars.append(tuple(map(int,input().split()))) # 입력값 그대로 튜플로 받는다.
pillars.append((1001,0)) #인덱스 에러 방지
pillars.sort() # 정렬

# 가장 높은 건물 기준으로 체크할 것이기 때문에
max_index, max_height = max(pillars, key=lambda a:a[1]) # 최대값
sum_height = max_height # 모든 합계

idx_save = 0 # 가장 높이가 높은 수 이외의 
height = 0 # 세로 높이
for idx in range(len(pillars) - 1): #왼쪽 기둥보다 높으면 다음 기둥까지 사각형
    if pillars[idx][0] < max_index: # 중간지점보다 낮을 경우
        if pillars[idx][1] >height: # 지붕 높이 검출
            height = pillars[idx][1]
            sum_height += abs(pillars[idx][0] - pillars[idx + 1][0]) *height
    else:
        idx_save = idx
        break

height = 0 # 세로 높이
for idx in range(len(pillars)-1, idx_save,-1): # 
    if pillars[idx][1] >height: # 지붕 높이 검출
        height = pillars[idx][1]
        sum_height += abs(pillars[idx - 1][0] - pillars[idx][0]) *height
    
print(sum_height)