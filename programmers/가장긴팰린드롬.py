def solution(s):
    answer = 0
    right = len(s) - 1
    
    for left in range(len(s)):
        for right in reversed(range(len(s))):
            if left > right or right - left  < answer:
                break
            if s[left] == s[right]:
                i = 0
                while True:
                    if s[left + i] != s[right - i]:
                        break
                    i += 1
                    if left + i > right - i:
                        # 정답체크
                        answer = max(answer, right - left + 1)
                        break
                    
                    
            
    return answer