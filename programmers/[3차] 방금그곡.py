# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answers = []

    for musicinfo in musicinfos:
        start, end, title, music_base = musicinfo.split(',')
        music_len = len(music_base)
        hour, minute = start.split(':')
        start = int(hour) * 60 + int(minute)
        hour, minute = end.split(':')
        end = int(hour) * 60 + int(minute)

        time = end - start
        music = ''
        index = 0
        for _ in range(time):
            music += music_base[index % music_len]
            index += 1
        print(music)
        if m in music:
            answers.append((time, title))
        
    return answers

a = "ABCDEFG"	
b = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(a,b))
a = "CC#BCC#BCC#BCC#B"	
b = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(a,b))
a = "ABC"	
b = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(a,b))