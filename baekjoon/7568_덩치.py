#더 큰 덩치가 몇 명인지 체크하는 것이 핵심
N = int(input())

#데이터 넣을 Dictionary
dicts = [{'weight':None,'height':None,'rank':1}for _ in range(N)]
for i in range(N):
    dicts[i]['weight'], dicts[i]['height'] = map(int, input().split())

#검증 #O(n^2/2)일까?
for i in range(N): #i는 검증할 캐릭터
    for j in range(N): #j는 비교대상
        if j > i:
            #i가 더 쎌 때
            if dicts[i]['weight'] < dicts[j]['weight'] and dicts[i]['height'] < dicts[j]['height']:
                dicts[i]['rank'] += 1
            #elif dicts[i]['weight'] < dicts[j]['weight'] and dicts[i]['height'] <= dicts[j]['height']:
            #    dicts[i]['rank'] += 1
            #j가 더 쎌 때
            elif dicts[i]['weight'] > dicts[j]['weight'] and dicts[i]['height'] > dicts[j]['height']:
                dicts[j]['rank'] += 1
            #elif dicts[i]['weight'] > dicts[j]['weight'] and dicts[i]['height'] >= dicts[j]['height']:
            #    dicts[j]['rank'] += 1

#출력
for dic in dicts:
    print(dic.get('rank'),end = ' ')