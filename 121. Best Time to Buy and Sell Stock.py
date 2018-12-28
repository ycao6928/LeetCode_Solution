class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
       
        #eg, [7, 1, 5, 3, 6, 4]
        #dont have to do brute force and double loop
        #can do this in single loop 
        #why?
        #because if we know 1 is the lowest
        #then no need to check for 3, ie, no need to check 6 - 3, 6 - 4
        #because , obviously, can't get any greater than 6 - 1 
        
        #it just that, everytime we encouter a new minimum, we need to recompute the profit
        #also , everytime the current number is higher than the minimum, we need to compute to profit (to see whether the current profit is greater than the max profit)
        
        minimumprice = 99999
        maxprofit = 0 
        for currprice in prices:
            if currprice > minimumprice:
                if currprice - minimumprice > maxprofit:
                    maxprofit = currprice - minimumprice
            elif currprice < minimumprice:
                minimumprice = currprice
                
        return maxprofit
     
        #eg, [7, 1, 5, 3, 6, 4] #solution would be 1 and 6 
        #start with 
        #minprice = 99999, profit = 0 
        
        # check 7
        # 7 < 99999 (the current min)
        # so minprice = 7, profit = 0 
        
        #check 1
        # 1 < 7 (the current min)
        # minprice = 1, profit = 0
        
        #check 5
        # 5 > 1 (indiate there is profit )and 
        # 5 - 1 > profit 0
        # minprice = 1, profit = 4
        
        #check 3
        #3 > 1 (indicate there is profit)
        # 3 - 1 not greater than profit 4 
        #don't change 
        #minprice = 1, profit = 4
        
        #check 6
        # 6 > 1(there is profit)
        # also 6 - 1 > the current profit of 4
        #minprice = 1, profit = 5
        
                
