#https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    visited = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    visited[0][0] = triangle[0][0]

    for idx, tri in enumerate(triangle):
        if idx != 0:
            for jdx, t in enumerate(tri):
                # 앞에꺼와 뒤에 것중 큰것
                # print(idx, jdx)
                if 0 < jdx < len(tri)-1:
                    if visited[idx-1][jdx-1] < visited[idx-1][jdx]:
                        visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx]
                    else:
                        visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx-1]
                elif jdx == 0:
                    visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx]
                elif jdx == len(tri)-1:
                    visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx-1]

    # print(visited)
    return max(visited[-1])

tr = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tr))