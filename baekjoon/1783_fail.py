##실패
x, y = map(int, input().split())
count = 0

if y >= 5 and x >= 5:
    count += 4
    while x >= 0:
        if x >= 7:
            x -= 6 
            count += 4
        else:
            if x == 6 : count += 4
            if x == 5 : count += 4
            if x == 4 : count += 3
            if x == 3 : count += 3
            if x == 2 : count += 2
            if x == 1 : count += 2
            if x == 0 : count += 1
            break
elif y >= 5 and x <= 4:
    count = x
else:
    max_x = x
    max_y = y
    while y <= max_y and x <= max_x and count <= 6:
        count += 1
        if y >= 2 :
            x += 1
            y -= 2
        elif y <= max_y - 2 :
            x += 1
            y += 2
        elif y >= 1:
            x += 2
            y -= 1
        elif y <= max_y - 1 :
            x += 2
            y += 1


'''
while y <= max_y and x <= max_x and count <= 4:
    count += 1
    if y >= 2 :
        x += 1
        y -= 2
    elif y <= max_y - 2 :
        x += 1
        y += 2
    elif y >= 1:
        x += 2
        y -= 1
    elif y <= max_y - 1 :
        x += 2
        y += 1
'''

print(count)