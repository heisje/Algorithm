from collections import deque
import heapq

def timeToSec(time):
    hour, minute, second = map(int, time.split(":"))
    minute += hour * 60
    second += minute * 60
    return second

def solution(play_time, adv_time, logs):
    # 시작시간을 기준으로 heapq에 넣는다.
    # 힙큐를 탐색하면서 가장 오래 겹치는 곳을 찾는다.
    play_sec = timeToSec(play_time)
    adv_sec = timeToSec(adv_time)
    # print(play_sec, adv_sec)
    #secLogs = []
    countMap = [0 for _ in range(play_sec+2)]
    for log in logs:
        before, after = log.split("-")
        # print(timeToSec(before), timeToSec(after)+1)
        #secLogs.append((timeToSec(before), timeToSec(after)))
        countMap[timeToSec(before)] += 11111
        countMap[timeToSec(after)+1] += -1
    
    for idx in range(1, len(countMap)):
        countMap[idx] = countMap[idx] + countMap[idx - 1]

    
    #print(list(zip([idx for idx in range(len(countMap))], countMap)))


    answer = 0
    max_count = sum(countMap[0:adv_sec+1])
    # print(max_count)
    sum_count = max_count
    for idx in range(adv_sec+1, len(countMap)):
        sum_count = sum_count + countMap[idx] - countMap[idx-(adv_sec)] 
        if sum_count > max_count:
            answer = idx - adv_sec
            max_count = sum_count

    # print(max_count)
    # print(answer)
    hour = answer // 3600
    minute = (answer % 3600) // 60
    sec = (answer % 3600) % 60
    
    return f'{hour}:{minute}:{sec}'

print(solution("02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))