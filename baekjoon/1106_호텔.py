C, N = map(int, input().split())
li = list()
for n in range(N):
    money, people = map(int, input().split())
    li.append([money, people])

li.sort()

mapped = [0 for _ in range(C+3)]    # value는 최소 금액

for cur_people in range(1, C+1):
    min_money = 10000000000000     # 최소 금액
    for add_money, add_people in li:
        # 현재 최소금액 기준 인구를 구하려면, 이전의 인구에서 뽑아서 써야한다.
        before_people = cur_people - add_people
        if before_people < 0:
            before_people = 0
        
        before_money = mapped[before_people]

        # 이전의 금액 + 현재금액
        if before_money + add_money < min_money:
            min_money = before_money + add_money

        # 4원을 채우기 위해 필요한 금액
        # 1원에서 3원을 더한다.
        # 3원에서 1원을 더한다.
        mapped[cur_people] = min_money


print(mapped[C])