class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1, 1 # start at one and one as def value since we are looping n-1 times 
        for i in range(n-1):
            temp = one #save one 
            one = one + two
            two = temp
        return one 