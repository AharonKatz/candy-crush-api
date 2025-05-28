from typing import List

def crush(board: List[List[int]]) -> dict:
    rows, cols = len(board), len(board[0])
    changed = True
    combo = 0

    def dfs(r, c, color, group, visited):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or board[r][c] != color):
            return
        visited.add((r, c))
        group.append((r, c))
        dfs(r+1, c, color, group, visited)
        dfs(r-1, c, color, group, visited)
        dfs(r, c+1, color, group, visited)
        dfs(r, c-1, color, group, visited)

    def apply_gravity():
        for c in range(cols):
            write_row = rows - 1
            for r in reversed(range(rows)):
                if board[r][c] != 0:
                    board[write_row][c] = board[r][c]
                    if write_row != r:
                        board[r][c] = 0
                    write_row -= 1

    while changed:
        changed = False
        to_crush = [[False]*cols for _ in range(rows)]
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 0 and (i, j) not in visited:
                    group = []
                    dfs(i, j, board[i][j], group, visited)
                    if len(group) >= 4:
                        changed = True
                        for r, c in group:
                            to_crush[r][c] = True

        for i in range(rows):
            for j in range(cols):
                if to_crush[i][j]:
                    board[i][j] = 0

        if changed:
            combo += 1
            apply_gravity()

    return {"board": board, "combo": combo}
