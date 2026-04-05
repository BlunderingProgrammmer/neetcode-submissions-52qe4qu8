class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW ,COL = len(grid),len(grid[0])
        visted = set()

        def dfs(r,c):
            if not(r in range(ROW)) or not(c in range(COL)) or grid[r][c] == 0 or (r,c) in visted:
                return 0 
            visted.add((r,c))
            #wrote teh dfs on my own pretty proud of that 
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        area = 0 
        for r in range(ROW):
            for c in range(COL):
                area = max(area,dfs(r,c))
        return area