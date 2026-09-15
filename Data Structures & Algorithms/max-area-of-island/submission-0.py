from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        width = len(grid[0])
        height = len(grid)

        for row in range(height):
            for column in range(width):
                if grid[row][column] != 1:
                    continue

                cur = 0
                q = deque()
                q.append((row, column))
                grid[row][column] = 2

                while q:
                    r, c = q.popleft()
                    cur += 1

                    if r > 0 and grid[r - 1][c] == 1:
                        q.append((r - 1, c))
                        grid[r - 1][c] = 2
                    if r < height - 1 and grid[r + 1][c] == 1:
                        q.append((r + 1, c))
                        grid[r + 1][c] = 2
                    if c > 0 and grid[r][c - 1] == 1:
                        q.append((r, c - 1))
                        grid[r][c - 1] = 2
                    if c < width - 1 and grid[r][c + 1] == 1:
                        q.append((r, c + 1))
                        grid[r][c + 1] = 2

                if cur > maxi:
                    maxi = cur

        return maxi

                

        