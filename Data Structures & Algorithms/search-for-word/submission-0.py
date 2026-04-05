class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS ,COL = len(board) , len(board[0])
        visted = set()
        def dfs(r,c,target_char_index):
            if target_char_index == len(word):
                return True #along with base case u also need a victory condition
            if (r not in range(ROWS) or
                (c not in range(COL)) or
                (r,c) in visted or
                board[r][c] != word[target_char_index]):
                return False
            visted.add((r,c))
            res = (
                dfs(r+1,c,target_char_index+1) or
                dfs(r-1,c,target_char_index+1) or
                dfs(r,c+1,target_char_index+1) or
                dfs(r,c-1,target_char_index+1)
            )
            visted.remove((r,c)) #cleaup backtrack step
            return res


        for i in range(ROWS):
            for j in range(COL):
                if dfs(i,j,0):
                    return True#0 cuz u are increamenting in dfs
        return False