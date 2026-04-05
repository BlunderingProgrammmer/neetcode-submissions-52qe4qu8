class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l,r = 0,len(matrix[0]) #set r off by one to make the code litle more intuitive
        top,bottom = 0,len(matrix) #again off by one set ...setting logic think about it for a bit
        while l<r and top<bottom:
            #for first row l->r
            #shifting rows
            for i in range(l,r):
                res.append(matrix[top][i])
            top+=1 # since offset by one
            #shifting columm
            # for 2nd row going down from r
            for i in range(top,bottom):
                res.append(matrix[i][r-1])
            r-=1
            if not(l<r and top<bottom):
                break
            #for getting the bottom row r->l
            for i in range(r-1,l-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            #for getting the left row-bottom>top
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res
        #most annoying part is logical range defination

