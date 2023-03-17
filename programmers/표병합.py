from collections import defaultdict
from copy import deepcopy

class Grid:
    data = []
    mergedData = [] # merge에 대한 mergedInx정보가 들어있는 데이터
    answer = []
    mergedInx = 1 # 쉽게 찾기 위한 mergedInx
    mergedDict = defaultdict(set)  # mergedInx로 이뤄진 실질적인 위치정보 딕셔너리

    def __init__(self):
        self.data = [["" for _ in range(51)]for _ in range(51)]
        self.mergedData = [[0 for r in range(51)]for c in range(51)]

    def update1(self, r, c, value):
        for pr, pc in self.mergedDict[self.mergedData[c][r]]:
            self.data[pc][pr] = value
        self.data[c][r] = value

    def update2(self, value1, value2):
        for c in range(51):
            for r in range(51):
                if self.data[c][r] == value1:
                    self.data[c][r] = value2

    def merge(self, r1, c1, r2, c2):
        # 같은 셀이면 무시
        if r1 == r2 and c1 == c2:
            return
        # 둘 다 값을 가지고 있을 때
        if self.data[c1][r1] and self.data[c2][r2]:
            self.data[c2][r2] = self.data[c1][r1] 
        # 하나만 값을 가지고 있을 때
        elif self.data[c2][r2]:
            self.data[c1][r1] = self.data[c2][r2] 
        elif self.data[c1][r1]:
            self.data[c2][r2] = self.data[c1][r1] 

        temp = set()
        temp.add((r1,c1))
        temp.add((r2,c2))
        for rc in self.mergedDict[self.mergedData[c1][r1]]:
            temp.add(rc)
        for rc in self.mergedDict[self.mergedData[c2][r2]]:
            temp.add(rc)
        
        self.mergedInx += 1
        self.mergedDict[self.mergedInx] = deepcopy(temp)
        
        for r, c in self.mergedDict[self.mergedInx]:
            self.data[c][r] == self.data[c1][r1]
            self.mergedData[c][r] = self.mergedInx
        
    def unmerge(self, r, c):
        temp = self.data[c][r]
        mergedTemp = self.mergedData[c][r]
        for pr, pc in self.mergedDict[mergedTemp]:
            self.mergedData[pc][pr] = 0
            self.data[pc][pr] = ""
        self.data[c][r] = temp
        
    def print(self, r, c):
        if self.data[c][r]:
            self.answer.append(self.data[c][r])
        else:
            self.answer.append("EMPTY")
        
    def __repr__(self):
        for y in range(50):
            print(self.data[y])
        return "출력끝"

def solution(commands):
    grid = Grid()
    for command in commands:
        cmd = command.split(" ")
        if cmd[0] == "UPDATE":
            if len(cmd) == 4:
                grid.update1(int(cmd[1]), int(cmd[2]), cmd[3])
            elif len(cmd) == 3:
                grid.update2(cmd[1], cmd[2])
        elif cmd[0] == "MERGE":
            grid.merge(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
        elif cmd[0] == "UNMERGE":
            grid.unmerge(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "PRINT":
            grid.print(int(cmd[1]), int(cmd[2]))
    print(grid)
    return grid.answer

# commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
# print(solution(commands))
commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(commands))
