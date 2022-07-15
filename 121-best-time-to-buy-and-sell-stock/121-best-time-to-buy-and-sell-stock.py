class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #left is for buying and r is for Selling
        maxP=0
        while r < len(prices):   #will go till the end of the array
            if prices[l]<prices[r]:
                profit= prices[r]-prices[l]
                maxP=max(profit,maxP)
            else:
                l=r
            r+=1
        return maxP
        