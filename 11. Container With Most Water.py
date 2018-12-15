class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) < 2:
            return 0
      
        maxarea = 0
        j = len(height)-1
        i = 0
        
        #for index in range(len(height)):
        #for some reasons.. using while loop is faster than using for loop o_O
        while i < j:
            temparea  =  min(height[i], height[j]) * (j - i)
            maxarea = max(maxarea,temparea)
            if height[i] < height[j]: #keep the longer one 
                i = i + 1 #ie, if the left one is shorter, go one step to the right 
            else:
                j = j - 1 #if the right one is shorter, go one step to the left 
        return maxarea
                
                
                
        
