class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [0, 1], [1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    area += 1
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans, bfs(i, j))
        return ans