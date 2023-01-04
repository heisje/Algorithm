# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 0

    group = []
    group.append(routes[0])
    for i in range(1, len(routes)):
        for j in range(len(group)):
            # 교집합이 존재하면 누적하고 break
            if group[j][0] <= routes[i][0] <= group[j][1] or group[j][0] <= routes[i][1] <= group[j][1]:
                if group[j][0] < routes[i][0]:
                    group[j][0] = routes[i][0]
                if routes[i][1] < group[j][1]:
                    group[j][1] = routes[i][1]
                break
        # 교집합이 존재하지 않으면
        else:
            group.append(routes[i])

    
    print(group)

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))