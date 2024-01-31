# 1. 장르별로 많이 재생된 노래 2개씩 모아야됨
# 1. 속한 노래가 많이 재생된 장르 수록
# 2. 장르 내에 많ㅇ이 재생된 노래 먼저 수록
# 3. 재생횟수가 같으면 고유번호가 낮은 노래
import heapq
from collections import defaultdict
def solution(genres, plays):
    N = len(genres)
    dic = dict()
    sum_ = defaultdict(int)
    for n in range(N):
        if not dic.get(genres[n]):
            dic[genres[n]] = []
        heapq.heappush(dic[genres[n]], (-plays[n], n))
        sum_[genres[n]] += plays[n]
    
    best_album = []
    for key in dic:
        save = [-sum_[key]]
        save.append(heapq.heappop(dic[key]))
        if dic[key]:
            save.append(heapq.heappop(dic[key]))
        heapq.heappush(best_album, save)
    
    answer = []
    while best_album:
        temp = heapq.heappop(best_album)
        answer.append(temp[1][1])
        
        if len(temp) > 2:
            answer.append(temp[2][1])
    return answer