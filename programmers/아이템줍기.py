from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    rtg = []
    for r in rectangle:
        a, b, c, d = r
        rtg.append([a*2, b*2, c*2, d*2])
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    grid = [[0 for _ in range(102)]for _ in range(102)]
    
    for lbx, lby, rtx, rty in rtg:
        for y in range(lby, rty + 1):
            for x in range(lbx, rtx + 1):
                mark = 2
                if x == lbx or x == rtx:
                    mark = 1
                if y == lby or y == rty:
                    mark = 1
                grid[y][x] = max(grid[y][x], mark)
    
    # for y in range(len(grid)-1,0,-1):
    #         print(grid[y])
    dq = deque()
    dq.append((itemX, itemY, 0))
    while dq:
        x, y, cnt = dq.popleft()
        if x == characterX and y == characterY:
            return cnt // 2
        
        for gx, gy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= gx < 102 and 0 <= gy < 102 and grid[gy][gx] ==1:
                grid[gy][gx] = 2
                dq.append((gx, gy, cnt+1))
    