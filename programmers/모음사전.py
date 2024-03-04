def solution(word):
    answer = 0
    aeiou = ['A','E','I','O','U','']
    li = []
    def loop(n, pre):
        if n >= 5:
            li.append(''.join(pre))
            return
        for a in aeiou:
            if not a:
                li.append(''.join(pre))
            else:
                loop(n+1, pre+[a])
    
    
    loop(0,[])
    li.sort()
    
    return li.index(word)