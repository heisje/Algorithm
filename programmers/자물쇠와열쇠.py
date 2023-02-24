# 락의 그래프에서 맨 위 왼쪽부터 첫 번째로 기준을 잡는다.
# 네가지 방향으로 미리 돌려놓고, 기준점에 대입해본다.
def solution(key, lock):
    LOCK_LEN = len(lock)
    KEY_LEN = len(key)
    
    # Key 속성
    keyRotates = [[[0 for _ in range(0, len(key[0]))] for _ in range(0, len(key))] for _ in range(0,4)]
    keyDols = [[] for _ in range(0,4)]

    # 90도 돌리기
    for y in range(0, len(key)):
        for x in range(0, len(key[y])):
            keyRotates[0][x][KEY_LEN - 1 - y] = key[y][x]
            if key[y][x] == 1:
                keyDols[0].append((KEY_LEN - 1 - y,x))
                
    for i in range(1,4):
        for y in range(0, len(key)):
            for x in range(0, len(key[y])):
                keyRotates[i][x][KEY_LEN - 1 - y] = keyRotates[i-1][y][x]
                if keyRotates[i-1][y][x] == 1:
                    keyDols[i].append((KEY_LEN - 1 - y,x))
    
    # lock 구멍 찾기, trg로 전부 1일 경우 배제
    lockHoles = []
    trg = True
    for y in range(0, len(lock)):
        for x in range(0, len(lock[y])):
            if lock[y][x] == 0:
                lockHoles.append((x, y))
                trg = False
    if trg:
        return True

    # 락의 첫번째를 기준으로 모든 키의 값에 대입해본다.
    for i in range(0,4):                # 4방향 테스트
        for lockHole in lockHoles:      # 락 구멍을 전부 탐색
            holeX, holeY = lockHole
            for value in keyDols[i]:    # 키 돌기를 전부 탐색
                dolX, dolY = value

                # 돌기의 위치를 홀에 맞춘다.
                dX = holeX - dolX
                dY = holeY - dolY

                # lock x,y를 전부 돌면서, key와 맞는지 확인해본다.
                def check():
                    for y in range(0, len(lock)):
                        for x in range(0, len(lock[y])):
                            if 0 <= y-dY < len(keyRotates[i]) and 0 <= x-dX < len(keyRotates[i][0]):
                                if lock[y][x] == keyRotates[i][y-dY][x-dX] :
                                    return False
                            else:
                                if lock[y][x] == 0:
                                    return False
                    return True

                if check():
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))