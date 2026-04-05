class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW ,COL = len(matrix),len(matrix[0]) #no of items in a 2d array and 
        #col is no of items on a single list in side 2d array
        top,bot = 0,ROW-1 #ROW set to last list 
        while top <= bot:
            correct_list = (top+bot) // 2
            if target > matrix[correct_list][-1]:
                top = correct_list + 1
            elif target < matrix[correct_list][0]:
                bot = correct_list - 1
            else:
                break #only break out when condition is reach
        if not (top <= bot):
            return False
        row = (top+bot) // 2 #calc the row which we found in prev loop
        l , r = 0 , COL -1 # just get index of a list
        while l <= r:
            mid = (l+r) // 2
            if target > matrix[row][mid]:
                l = mid +1
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                return True
        return False #return false if u cant find it 