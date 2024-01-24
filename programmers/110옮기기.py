# 기존 풀이 111과 111뒤에 있는 110의 위치를 바꿔 풀었다.
# 기존 풀이의 문제점: 맨 뒤에 있는 0과 1을 찾지 못한다.

# 개선된 풀이: 
# 110을 모두 뺀 후,
# 11, 0(맨뒤), 1을 찾은 후
# 차례대로 조건을 조사하여
# 11인 경우 앞에
# 0인 경우 뒤에
# 1인 경우 앞에 놓는다.

def solution(s):
    answer = []
    
    for ss in s:
        temp_ss = []
        cnt = 0  
        idx = 0
        for num in ss:
            if num == '0' and temp_ss[-2:] == ['1', '1']:
                cnt += 1
                temp_ss.pop()
                temp_ss.pop()
            else:
                temp_ss.append(num)
        temp_ss = ''.join(temp_ss)
                    
        
        # print(cnt)
            
        if cnt == 0 :
            answer.append(temp_ss)
            continue
        
        if cnt >= 1 and temp_ss == '':
            temp_ss = '110' * cnt
            answer.append(temp_ss)
            continue
        
        if cnt >= 1 and temp_ss == '1':
            temp_ss = '110' * cnt + '1'
            answer.append(temp_ss)
            continue
        
        idx = temp_ss.find('11')
        if cnt >= 1 and idx >= 0:
            temp_ss = temp_ss[:idx] + '110' * cnt + temp_ss[idx:]
            answer.append(temp_ss)
            continue
            
        if cnt >= 1 :
            t = temp_ss[::-1]
            idx = t.find('0')
            if idx >= 0:
                idx_0 = len(temp_ss) - 1 - idx
                temp_ss = temp_ss[:idx_0+1]+'110'*cnt+temp_ss[idx_0+1:]
            answer.append(temp_ss)
            continue
            
    return answer