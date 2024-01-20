from collections import deque

def solution(board):
    SIZE = len(board)  # 보드의 크기 (N x N)
    ROW_WISE, COLUMN_WISE = range(2)  # 방향을 나타내는 상수 (가로 및 세로)
    OPEN, WALL = range(2)  # 열린 경로와 벽을 나타내는 상수
    START = (0, 0, ROW_WISE)  # 시작 지점의 초기 위치와 방향
    END_POINT = (SIZE-1, SIZE-1)  # 도착 지점의 위치
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 상하좌우로 이동할 때 변경되는 좌표

    queue = deque([START])  # BFS를 위한 큐 초기화
    visited = set()  # 이미 방문한 좌표를 추적하기 위한 집합 초기화
    visited.add(START)  # 시작 지점을 방문한 것으로 표시
    moves_count = 0  # 이동 횟수 초기화

    def _is_in_range(r, c):
        """주어진 좌표 (r, c)가 보드 내에 있는지 확인"""
        return 0 <= r < SIZE and 0 <= c < SIZE

    def _is_open(r, c):
        """주어진 좌표 (r, c)가 열린 경로인지 확인"""
        return board[r][c] == OPEN

    def _is_ok(r, c):
        """주어진 좌표 (r, c)가 범위 내에 있고 열린 경로인지 확인"""
        return _is_in_range(r, c) and _is_open(r, c)

    def _yield_moves_rowwise(r, c):
        """주어진 좌표 (r, c)에서 가로 방향으로 이동 가능한 좌표 생성"""
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            # 새로운 위치와 그 다음 위치가 모두 열린 경로인 경우에만 이동 가능
            if _is_ok(new_r, new_c) and _is_ok(new_r, new_c+1):
                yield (new_r, new_c, ROW_WISE)

        # 가로 방향에서 세로 방향으로 이동 가능한 경우 고려
        if _is_ok(r+1, c) and _is_ok(r+1, c+1):
            yield (r, c, COLUMN_WISE)
            yield (r, c+1, COLUMN_WISE)
        if _is_ok(r-1, c) and _is_ok(r-1, c+1):
            yield (r-1, c, COLUMN_WISE)
            yield (r-1, c+1, COLUMN_WISE)

    def _yield_moves_columnwise(r, c):
        """주어진 좌표 (r, c)에서 세로 방향으로 이동 가능한 좌표 생성"""
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            # 새로운 위치와 그 다음 위치가 모두 열린 경로인 경우에만 이동 가능
            if _is_ok(new_r, new_c) and _is_ok(new_r+1, new_c):
                yield (new_r, new_c, COLUMN_WISE)

        # 세로 방향에서 가로 방향으로 이동 가능한 경우 고려
        if _is_ok(r, c-1) and _is_ok(r+1, c-1):
            yield (r, c-1, ROW_WISE)
            yield (r+1, c-1, ROW_WISE)
        if _is_ok(r, c+1) and _is_ok(r+1, c+1):
            yield (r, c, ROW_WISE)
            yield (r+1, c, ROW_WISE)

    while queue:
        moves_count += 1

        for _ in range(len(queue)):
            r, c, direction = queue.popleft()

            if direction == ROW_WISE:
                yield_func = _yield_moves_rowwise
            else:
                yield_func = _yield_moves_columnwise

            for new_coord in yield_func(r, c):
                if new_coord not in visited:
                    queue.append(new_coord)
                    visited.add(new_coord)

                    r, c, direction = new_coord
                    # 도착 지점에 도달한 경우 이동 횟수 반환하고 함수 종료
                    if (r, c+1) == END_POINT or (r+1, c) == END_POINT:
                        return moves_count

# 함수를 호출하여 최단 경로의 이동 횟수를 찾을 수 있습니다.
