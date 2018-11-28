
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #first create empty array of size n+3 (need 0, 1, 2)
        array = [0]*(3+n)
        array[1] = 1
        array[2] = 2
        
        #set to n + 1
        #so that, when n = 3
        #for i in range (3, 4)
        # array[3] = array[2] + array[1]
        #otherwise won't run 
        for i in range(3,n+1):
            array[i] = array[i-1] + array[i-2]
    
        return array[n] 

       
