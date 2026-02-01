class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(0,len(prices)):
            if prices[i]==i:
                break
        stockbuy=i
                       

        maxprice=max(prices[stockbuy:])
        if stockbuy==0:
            profit=0
            return profit
        else:
            profit=maxprice-stockbuy
            if profit <= stockbuy:
                return 0
            else:
                return profit

        
        
        