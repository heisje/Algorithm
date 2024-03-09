def timeToMinute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def solution(plans):
    answer = []
    plans.sort(key = lambda x:x[1])
    stack = []
    
    # 해야할 과제를 스택에 넣는다.
    for i in range(0, len(plans)-1):
        text, strTime, strToSpendTime = plans[i]
        time, toSpendTime = timeToMinute(strTime), int(strToSpendTime)
        
        nextText, nextStrTime, strNextToSpendTime = plans[i+1]
        nextTime, nextToSpendTime = timeToMinute(nextStrTime), int(strNextToSpendTime)
        
        freeTime = nextTime - time
        if freeTime < toSpendTime:
            stack.append((text, toSpendTime-freeTime))
            continue
        elif freeTime >= toSpendTime:
            answer.append(text)
            freeTime = freeTime - toSpendTime
            
            while stack and freeTime:
                oldText, oldToSpendTime = stack.pop()
                if freeTime < oldToSpendTime:
                    stack.append((oldText, oldToSpendTime - freeTime))
                    break
                elif freeTime >= oldToSpendTime:
                    answer.append(oldText)
                    freeTime -= oldToSpendTime
    answer.append(plans[-1][0])
    while stack:
        text, _ = stack.pop()
        answer.append(text)
    
    return answer