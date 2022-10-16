def solution(record): 
    name_change = dict()
    answer = []
    for r in record:
        code, user_id, *nickname = r.split()
        if nickname:
            name_change[user_id] = nickname[0]
        if code == "Enter":
            answer.append((user_id, "님이 들어왔습니다."))
        elif code == "Leave":
            answer.append((user_id, "님이 나갔습니다."))
    
    
    for idx, value in enumerate(answer):
        user_id, txt = value
        answer[idx] = name_change[user_id] + txt
    return answer

#import sys
#sys.stdin = open('./input.txt')
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

#LV.2 / 30분
