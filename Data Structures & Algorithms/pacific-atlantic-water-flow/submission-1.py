class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows , colm = len(heights),len(heights[0])
        pacific , atlantic = set(),set() 
        #define the dfs logic
        def dfs(r,c,visted_set,prev_height):
            #base case
            if (r not in range(Rows) or (c not in range(colm)) or (r,c) in visted_set or heights[r][c] < prev_height):
                return
            visted_set.add((r,c))
            dfs(r+1,c,visted_set,heights[r][c])
            dfs(r-1,c,visted_set,heights[r][c])
            dfs(r,c+1,visted_set,heights[r][c])
            dfs(r,c-1,visted_set,heights[r][c])
        
        #call teh function to get the hash set
        #define all points in 0 Rows
        for r in range(Rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,colm-1,atlantic,heights[r][colm-1])
        #define all points in last colm
        for c in range(colm):
            dfs(0,c,pacific,heights[0][c])
            dfs(Rows-1,c,atlantic,heights[Rows-1][c])

        #brute force to check and compare
        res = []
        for r in range(Rows):
            for c in range(colm):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

        #bug i had put heights[r][c] everywher instead of grid coordinates