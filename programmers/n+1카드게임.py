# 카드를 뽑고 사용해야할 때 코인을 쓴다.
# 필요한 코인 수 기준으로 힙으로 정렬해둔다.
import heapq
def solution(coin, cards):
    N = len(cards)
    duo = dict()
    for n in range(1, N//2+1):
        duo[n] = N+1-n
        duo[N+1-n] = n
    
    # 처음 카드뽑기
    hand = set(cards[:N//3])  # 내 손패
    hq = [] # 현재 턴 넘길 수 있는 개수
    other = set() # 
    
    n = 0
    passCard = set()
    while hand and n < N//3:
        # 현재 가지고 있는 카드 중 가능한 것이 있으면
        if duo[cards[n]] in hand:
            heapq.heappush(hq, 0)
            hand.remove(cards[n])
            hand.remove(duo[cards[n]])
            passCard.add(duo[cards[n]])
        # elif cards[n] not in passCard and duo[cards[n]] not in hand:
        #     pass
        #     other.add(cards[n])
        n += 1
    
    answer = 1
    
    coinInfo = dict()
    for h in list(hand):
        coinInfo[h] = 0
    
    for n in range(N//3, N, 2):
        for new in [cards[n], cards[n+1]]:
            
            if duo[new] in hand:
                hand.remove(duo[new])
                heapq.heappush(hq, coinInfo[duo[new]] + 1)
            else:
                hand.add(new)
                coinInfo[new] = 1
            #print('new', new, hand,hq)
                
        if hq:
            coin -= heapq.heappop(hq)
            #print(coin, hq)
            if coin < 0:
                return answer
            else:
                answer += 1
        else:
            return answer
        n += 2
    return answer