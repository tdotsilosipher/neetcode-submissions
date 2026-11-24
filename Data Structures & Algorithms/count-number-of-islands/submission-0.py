class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #directions (row, col)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #len of row and col
        rows, cols = len(grid), len(grid[0])

        islands = 0

        #bfs
        def bfs(r, c):
            # queue for bfs, set (r,c) to 0 and append
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                r, c = q.popleft()
                #check directions
                # check limits min and max and if "0"
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
