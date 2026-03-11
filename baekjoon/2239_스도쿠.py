# 포인트 하나 마다 검사
# row 9
# col 9
# grid 9
_SET = 0b1111111110  # 1-9를 이진수로 표현 (비트 1-9가 모두 1)

def getGridIndex(row, col) -> int:
    return row // 3 + (col // 3) * 3

def getGridSet(row, col) -> int:
    num = getGridIndex(row, col)
    return gridSet[num]

def getRowSet(row, col) -> int:
    return rowSet[col]

def getColSet(row, col) -> int:
    return colSet[row]

def getAbleNum(스도쿠, row, col) -> int:
    # 비트 OR 연산으로 합집합을 구하고, NOT으로 차집합을 구함
    used = getRowSet(row, col) | getColSet(row, col) | getGridSet(row, col)
    return _SET & ~used

스도쿠 = []
rowSet: list[int] = [0] * 9  # 이진수로 표현된 set
colSet: list[int] = [0] * 9  # 이진수로 표현된 set
gridSet: list[int] = [0] * 9  # 이진수로 표현된 set
ablesSet: list[list[int]] = [[0] * 9 for _ in range(9)]  # 이진수로 표현된 set
startX = -1
startY = -1

for i in range(0, 9):
    스도쿠.append(list(input().split()))
    


# for y in range(0, 9):
#     for x in range(0, 9):
#         num = 스도쿠[y][x]
#         if num != 0:
#             # 비트 OR 연산으로 숫자 추가
#             bit_mask = 1 << num
#             rowSet[x] |= bit_mask
#             colSet[y] |= bit_mask
#             gridSet[getGridIndex(y, x)] |= bit_mask
#             ablesSet[y][x] = bit_mask
#         if num == 0:
#             startX = x
#             startY = y

# stack = [(num, x, y)]
# ables = getAbleNum(스도쿠, startY, startX)
# ablesSet[startY][startX] = ables

# while True:
#     trg = False
#     for y in range(0, 9):
#         for x in range(0, 9):
#             if 스도쿠[y][x] == 0:
#                 ables = getAbleNum(스도쿠, y, x)
#                 ablesSet[y][x] = ables
                
#                 # 이진수에서 1의 개수를 세어 가능한 숫자 개수 확인
#                 if bin(ables).count('1') == 1:
#                     # 가장 낮은 비트 위치를 찾아 숫자 추출
#                     num = (ables & -ables).bit_length()
#                     스도쿠[y][x] = num
#                     bit_mask = 1 << num
#                     rowSet[x] |= bit_mask
#                     colSet[y] |= bit_mask
#                     gridSet[getGridIndex(y, x)] |= bit_mask
#                     trg = True

#     if trg == False:
#         break

# 결과 출력
for row in 스도쿠:
    print(*row)
