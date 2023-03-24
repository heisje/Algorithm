from collections import deque

def solution(n, t, m, old_timetable):
    answer = ''
    # timetable을 m으로 전부 변환시킨다.
    # 시작시간도 m로 변환시킨다.
    # 1분이 지날 때 마다 체크한다.
    #   사람이 들어오면 dq에 넣어준다.
    #   정시가 되면 사람들을 뺀다.
    # 종료조건1 : 시간이 다됐는데, 마지막 빠지는 사람일 때
    #   마지막 빠지는 사람과 같은 시간
    #   같은 시간일때 안되는 경우에는 1시간 빠르게
    # 종료조건2 : 모든 대기열을 마무리 했을때
    #   최대 시간을 리턴

    # timetable을 m으로 전부 변환시킨다.
    timetable = list()
    for idx, tt in enumerate(old_timetable):
        hour, minute = tt.split(':')
        minute = int(hour) * 60 + int(minute)
        timetable.append({'idx':idx, 'minute':minute})
    print(timetable)
    timetable.sort(key=lambda x: x['minute'])
    timetable = deque(timetable)
    print(timetable)
    # 순환버스시간도 m로 변환시킨다.
    # 9시 = 540
    bus = deque(540+t*nn for nn in range(n))
    print(bus)

    # 로직
    wait = deque()
    save = {'idx':0, 'minute':0} # 마지막으로 빠진 사람
    bus_save_time = 0 # 마지막으로 빠진 버스
    bus_save_li = [] # 마지막으로 빠진 버스
    for time in range(0, 1439):
        while timetable and timetable[0]['minute'] == time:
            wait.append(timetable.popleft())

        if bus and bus[0] == time:
            bus_save = bus.popleft()
            temp = []
            for _ in range(m):
                if wait:
                    save = wait.popleft() 
                    temp.append(save)
            if len[temp] < m:
                save({"minute":time})

            bus_save_li.append(temp)
        
        if not bus:
            if timetable:
                pass
            break
            

    answer = f"{str(save['minute'] // 60).zfill(2)}:{str(save['minute'] % 60).zfill(2)}"

    return answer

print(solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,	10,	2,	["09:10", "09:09", "08:00"]))

