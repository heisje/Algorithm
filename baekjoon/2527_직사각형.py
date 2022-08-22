import sys
sys.stdin = open('input.txt')

for _ in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = map(int, input().split())
    b = [[(lx1 + rx1)/2,(ly1 + ry1)/2,(rx1-lx1)/2,(ry1-ly1)/2],[(lx2 + rx2)/2,(ly2 + ry2)/2,(rx2-lx2)/2,(ry2-ly2)/2]]

    result = 'a'
    #print(b[0][0] - b[0][2] <= b[1][0] + b[1][2] <= b[0][0] + b[0][2], b[0][0] - b[0][2] <= b[1][0] - b[1][2] <= b[0][0] + b[0][2], b[0][1] - b[0][3] <= b[1][1] + b[1][3] <= b[0][1] + b[0][3], b[0][1] - b[0][3] <= b[1][1] - b[1][3] <= b[0][1] + b[0][3])
    #print(b[0][0],b[0][2],b[1][0], b[1][2],b[0][0], b[0][2])
    if (b[0][0] - b[0][2] <= b[1][0] + b[1][2] <= b[0][0] + b[0][2] or b[0][0] - b[0][2] <= b[1][0] - b[1][2] <= b[0][0] + b[0][2]) \
            and (b[0][1] - b[0][3] <= b[1][1] + b[1][3] <= b[0][1] + b[0][3] or b[0][1] - b[0][3] <= b[1][1] - b[1][3] <= b[0][1] + b[0][3]): #x,y가 겹치면
        pass
    else:
        result = 'd'

    #if b[0][0] + b[0][2] == b[1][0] + b[1][2]:
    #    pass
    #if b[0][0] + b[0][2] == b[1][0] + b[1][2]:
    #    pass
    print(b)
    print(result)

    '''
    b1_xy = [lx1, ly1]
    b1_wh = [rx1 - lx1, ry1 - ly1]
    b2_xy = [lx2, ly2]
    b2_wh = [rx2 - lx2, ry2 - ly2]

    if b1_xy[0] == b2_xy[0]:
        if b1_xy[1] == b2_xy[1]: #만약 x y 다 같으면
            print('a')
        elif b1_xy[1] > b2_xy[1]: #만약 x가 같으면 y로 순서비교
            b1_xy, b2_xy = b2_xy, b1_xy
            b1_wh, b2_wh = b2_wh, b1_wh
    elif b1_xy[0] > b2_xy[0]: #x로 순서비교
        b1_xy, b2_xy = b2_xy, b1_xy
        b1_wh, b2_wh = b2_wh, b1_wh
    if b1_xy[0] + b1_wh[0] < b2_xy[0]: #따로 떨어져있음
        print('d')
    '''


