import sys
sys.stdin = open('input.txt')

for _ in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = map(int, input().split())

    box1_x = [lx1, rx1]
    box1_y = [ly1, ry1]

    box2_x = [lx2, rx2]
    box2_y = [ly2, ry2]

    if (box1_x[0] <= box2_x[0] <= box1_x[1] or box1_x[0] <= box2_x[1] <= box1_x[1]) and \
        (box1_y[0] <= box2_y[0] <= box1_y[1] or box1_y[0] <= box2_y[1] <= box1_y[1]):

        a = list(set(range(box1_x[0], box1_x[1] + 1)) & set(range(box2_x[0], box2_x[1] + 1)))
        x = [-1, 0]
        if a != []:
            x = [min(a), max(a)]
        a = list(set(range(box1_y[0], box1_y[1] + 1)) & set(range(box2_y[0], box2_y[1] + 1)))
        y = [-1, 0]
        if a != []:
            y = [min(a), max(a)]

        #print(x, y)
        if x[0] == x[1] and y[0] == y[1]:
            print('c')
        elif (x[0] == x[1] and y[0] != y[1]) or (x[0] != x[1] and y[0] == y[1]):
            print('b')
        else:
            print('a')

    else:
        print('d')



