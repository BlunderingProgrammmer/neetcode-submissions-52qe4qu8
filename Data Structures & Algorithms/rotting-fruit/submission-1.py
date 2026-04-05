class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0 
        q = collections.deque()
        fresh_fruit_count = 0 
        ROW,COL = len(grid),len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        #preprossesing to get initial fresh fruits and rotten fruits
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh_fruit_count +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        while q:
            time+=1
            lenQ = len(q)#snapshot for multi source bfs
            for _ in range(lenQ):
                r,c = q.popleft()# rotten fruits
                for dr,dc in directions:
                    new_r,new_c = r+dr,c+dc
                    if (new_r in range(ROW) and (new_c in range(COL) and grid[new_r][new_c] == 1)):
                        grid[new_r][new_c] = 2
                        q.append((new_r,new_c))
                        fresh_fruit_count -=1
                        
        if fresh_fruit_count:
            return -1
        elif time:
            return time-1
        elif time == 0:
            return 0
