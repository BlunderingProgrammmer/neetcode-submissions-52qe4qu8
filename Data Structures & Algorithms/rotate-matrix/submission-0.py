class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0,len(matrix)-1
        while l < r:
            # for the i logic think about position in a 3*3 square matrix image niggaa
            for i in range(r-l):
                top ,bottom = l ,r #since its square matrix and the way 2d array is access think u will see it
                topleft = matrix[top][l+i] #save in temp and then replace the the empty spce in reverese to save space
                matrix[top][l+i] =  matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topleft
            #only need to increamet l and r since square matrix and its updated in for loop
            l+=1
            r-=1