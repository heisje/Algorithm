# 최대 HP는 이분탐색으로 찾는다.
# 안의 요소는 구현이다.
import sys, math
input = sys.stdin.readline

class HERO:
    def __init__(self, hp, atk) -> None:
        self.hp = hp
        self.maxHp = hp
        self.atk = atk

    def fight(self, monsterATK, monsterHP):
        heroAtkCount = math.ceil(monsterHP / self.atk)
        monsterAtkCount = math.ceil(self.hp / monsterATK)
        if heroAtkCount <= monsterAtkCount:
            self.hp -= (heroAtkCount - 1) * monsterATK
            return True
        if heroAtkCount > monsterAtkCount:
            return False

    def heal(self, upATK, upHP):
        self.atk += upATK
        self.hp += upHP
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return True
    

N, ATK = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

left, right = 1, 1000000*123456*1000000
answer = 0
while left <= right:
    center = (left+right) // 2

    hero = HERO(center, ATK)
    result = True
    for type, a, h in rooms:

        if type == 1:
            result = hero.fight(a,h)
        if type == 2:
            result = hero.heal(a,h) 
    
        # 던전 공략 실패, hp를 더 늘린다.
        if result == False:
            break
    
    # 던전 공략 실패, hp를 더 늘린다.
    if result == False:
        left = center + 1

    # 공략 성공. hp를 낮춰도 되는지 시험한다.
    elif result == True:
        answer = center
        right = center - 1

print(answer)