def solution(beginning, target):
    global answer
    
    answer = float('INF')
    yN = len(beginning)
    xN = len(beginning[0])
    
    def change_point(n):
        return abs(n - 1)
    
    def change_line(graph, x_or_y, i):
        if x_or_y == 'y':
            for x in range(xN):
                graph[i][x] = change_point(graph[i][x])
                
        if x_or_y == 'x':
            for y in range(yN):
                graph[y][i] = change_point(graph[y][i])
    
    def check(graph):
        for x in range(xN):
            for y in range(yN):
                if graph[y][x] != target[y][x]:
                    return (x, y)
        return 1
    
    def loop(graph, vis_x, vis_y):
        global answer
        
        check_save = check(graph)
        if check_save == 1:
            answer = min(answer, xN + yN - len(vis_x) - len(vis_y))
            return
        
        if check_save[0] not in vis_x:
            change_line(graph, 'x', check_save[0])
            vis_x.add(check_save[0])
            loop(graph, vis_x, vis_y)
            vis_x.remove(check_save[0])
            change_line(graph, 'x', check_save[0])
            
        if check_save[1] not in vis_y:
            change_line(graph, 'y', check_save[1])
            vis_y.add(check_save[1])
            loop(graph, vis_x, vis_y)
            vis_y.remove(check_save[1])
            change_line(graph, 'y', check_save[1])
    if check(beginning) == 1:
        return 0
    loop(beginning, set(), set())
    if answer == float('INF') and check(beginning) != 1:
        return -1
    return answer