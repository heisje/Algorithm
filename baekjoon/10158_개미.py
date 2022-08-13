W, H = map(int, input().split()) #그리드 W H
x, y = map(int, input().split()) #개미위치 X Y
HOUR = int(input())              #시간 HOUR

def check(x, W):
    if ((x + HOUR) // W) % 2 == 0: # x + HOUR 가 짝수이면
        return (x + HOUR) % W      # 항상 이렇게 나온다
    else:
        return (W - (x + HOUR) % W) # 아닐 시엔 역전되서 나온다
print(check(x, W), check(y,H))