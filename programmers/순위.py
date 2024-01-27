# 모든 노드에 대해
# 위로 몇개
# 아래로 몇개인지 세보고
# 더한 값이 n개면 통과



def solution(n, results):
    answer = 0
    MAX = float('INF')
    man = [0 for _ in range(n+1)]
    wins = [[] for _ in range(n+1)]
    loses = [[] for _ in range(n+1)]
    for win, lose in results:
        wins[lose].append(win)
        loses[win].append(lose)

    up_cnt = [0 for _ in range(n+1)]
    down_cnt = [0 for _ in range(n+1)]

    win_cnts = [0 for _ in range(n+1)]
    lose_cnts = [0 for _ in range(n+1)]

    win_visited = set()
    lose_visited = set()
    master = [0]

    def loop(i, nodes, cnts, visited):
        if i in visited:
            return 

        visited.add(i)
        master[0] += 1

        for node in nodes[i]:
            loop(node, nodes, cnts, visited)

        return 

    for i in range(1, n+1):
        visited = set()
        master[0] = 0
        loop(i, wins, win_cnts, visited)
        win_cnts[i] = master[0]
        visited = set()
        master[0] = 0
        loop(i, loses, lose_cnts, visited)
        lose_cnts[i] = master[0]

    for i in range(1, n+1):
        if n == win_cnts[i] + lose_cnts[i] - 1:
            answer += 1

    return answer