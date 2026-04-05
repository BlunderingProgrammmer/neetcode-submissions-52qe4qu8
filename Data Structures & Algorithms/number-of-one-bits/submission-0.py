class Solution:
    def hammingWeight(self, n: int) -> int:
        #first logical solution:
        res = 0 
        while n: # means while n > 0 or n exists
            res += n % 2 #the n is logical and with 2 gives 1 if 1 ,0 if 0-> then add the result to array
            n = n >> 1 #bitwise rightshift operator by one 
        return res