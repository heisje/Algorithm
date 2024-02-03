# dfs로 시추 크기를 구하고 구한 값을 가로축만 있는 배열에 저장
# 저장하면서 최대값을 구하면됨
import sys
sys.setrecursionlimit(10**6)

def solution(land):
    answer = 0
    X = len(land[0])
    Y = len(land)
    visited = [[False for _ in range(X)] for _ in range(Y)]
    value = [0 for _ in range(X)]
    
    saveXandCnt = { "minX":float("INF"), "maxX":-float("INF"), "cnt":0 } # minX, maxX, cnt
    
    def loop(x, y):
        # print("loop", x, y, saveXandCnt)
        visited[y][x] = True
        land[y][x] = 0
        saveXandCnt["cnt"] += 1
        saveXandCnt["minX"] = min(saveXandCnt["minX"], x)
        saveXandCnt["maxX"] = max(saveXandCnt["maxX"], x)
        
        for gx, gy in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0 <= gx < X and 0 <= gy < Y and visited[gy][gx] is False and land[gy][gx] == 1:
                loop(gx, gy)
            
    for x in range(X):
        for y in  range(Y):
            # 계산 안된게 있는지 판별
            if land[y][x] == 0:
                continue
                
            if visited[y][x] is True:
                continue  
            elif visited[y][x] is False:
                # check
                loop(x, y)
                for loopX in range(saveXandCnt["minX"], saveXandCnt["maxX"]+1):
                    value[loopX] += saveXandCnt["cnt"]
                saveXandCnt = { "minX":float("INF"), "maxX":-float("INF"), "cnt":0 }
      
    return max(value)