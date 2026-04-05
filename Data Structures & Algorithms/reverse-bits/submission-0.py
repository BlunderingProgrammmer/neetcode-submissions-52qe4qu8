class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 #initialize buy zero
        for i in range(32): #iterate by 32 times since 32 bit integer
            #get
            bit = (n >> i) & 1 #order -> bit is shifted by i means it always ends in ones place -> & give 1 for 1 and 0 for 0
            #move and set
            #move -> bit << (31-i)-> shift the bit to its reverse spot by (31-i)
            #set -> res | with that number -> logical or operater combines 0 and 1 without effecting others
            res = res | bit << (31-i)
        return res

