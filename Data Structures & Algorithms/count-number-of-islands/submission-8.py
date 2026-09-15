from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        width = len(grid[0])
        height = len(grid)

        for row in range(height):
            for column in range(width):
                if grid[row][column] != '1':
                    continue

                num += 1
                q = deque()
                q.append((row, column))
                grid[row][column] = "2"

                while q:
                    r, c = q.popleft()

                    if r > 0 and grid[r - 1][c] == "1":
                        q.append((r - 1, c))
                        grid[r - 1][c] = "2"
                    if r < height - 1 and grid[r + 1][c] == "1":
                        q.append((r + 1, c))
                        grid[r + 1][c] = "2"
                    if c > 0 and grid[r][c - 1] == "1":
                        q.append((r, c - 1))
                        grid[r][c - 1] = "2"
                    if c < width - 1 and grid[r][c + 1] == "1":
                        q.append((r, c + 1))
                        grid[r][c + 1] = "2"

        return num

                

        