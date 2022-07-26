li = []
for _ in range(5):
    inputation = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
    if inputation == 'Done':
        break
    else:
        per, g = inputation.split()
        li += [int(per.rstrip('%')), int(g.rstrip('g'))],
print(li)
#소금의 양 구하기
salt = 0.0
water = 0.0
for i in li:
    salt += i[0] * 0.01 * i[1]
    water += i[1]
print(f'{round((salt/water),10)*100}% {round(water)}g')

