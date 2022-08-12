W, H = map(int, input().split()) #그리드 W H
x, y = map(int, input().split()) #개미위치 X Y
HOUR = int(input())              #시간 HOUR

ro_x = (x + HOUR) // W
ro_y = (y + HOUR) // H

print(ro_x, ro_y)
if ro_x:
    x = x % W
y = y % H

print(ro_x, ro_y)
print(x, y)
# #방향
# dr_x = 1
# dr_y = 1

# for hour in range(HOUR):
#     x += dr_x
#     y += dr_y

#     if 0 <= x + dr_x <= W: #모서리에 도착했을 때
#         pass
#     else:    
#         dr_x *= -1

#     if 0 <= y + dr_y <= H: #모서리에 도착했을 때
#         pass
#     else:   
#         dr_y *= -1
# print(x, y)
#     #print(f' x = {x}, y = {y}, dx = {dr_x}, dy = {dr_y}')
    

