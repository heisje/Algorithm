def solution(n, times):
    answer = float('INF')
    
    def find_time(target_time):
        temp = 0
        for time in times:
            temp += target_time // time
        return temp
    
    left = 0
    right = max(times) * n
    cnt = 0
    
    while left < right:
        cnt += 1
        center = (left + right) // 2
        temp = find_time(center)
        if temp >= n:
            right = center
        elif temp < n:
            left = center + 1
    
    return left