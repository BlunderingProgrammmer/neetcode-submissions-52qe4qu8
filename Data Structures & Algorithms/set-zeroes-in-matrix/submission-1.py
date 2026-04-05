class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS ,COL = len(matrix),len(matrix[0])
        # u need one variable for the first element of the col check
        rowzero = False

        #find out which and where to get the zeross
        for r in range(ROWS):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 
                    #check which value to update in this either the row_zero variable or inplace matrix
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True

        #set to 0 in two steps
        #get and set the inner matrix to 0
        #then the 0 columm and 0 row
        for r in range(1,ROWS):
            for c in range(1,COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        #now clear the outer shell meatrix left

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowzero:
            for c in range(COL):
                matrix[0][c] = 0

    
