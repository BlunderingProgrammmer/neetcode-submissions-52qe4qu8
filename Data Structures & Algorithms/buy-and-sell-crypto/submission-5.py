class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0 ,1 #trailing left and rigth pointers
        max_profit = 0 
        while r< len(prices):#r is  in bounds
            if prices[l] < prices[r]:#then it is a profitable transaction
                profits = prices[r] - prices[l]
                max_profit = max(max_profit,profits)
            else:
                l = r #if l ka value is higher than r ka price and r is main mover just directly equate l =r since we found the lowest price
            r+=1
        return max_profit