arr = [0,0]
누적치 = 0
for idx in range(10):
    if idx % 2 == 0:
        누적치 += 2
        arr.append(누적치)
    else:
        arr.append(누적치)
print(arr)