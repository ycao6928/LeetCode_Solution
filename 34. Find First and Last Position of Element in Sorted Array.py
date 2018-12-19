class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# because we are locating the leftmost (and rightmost) index containing target the algorithm does not terminate as soon as we find a match. 
# Instead, we continue to search until lo == hi and they contain some index at which target can be found.  

#when finding the leftmost index
#when min == max
#they are at the leftmost index


#when finding the rightmost index
#when min == max
#they are one index to the right of the actual rightmost index

#performs 2 binary search, log(n) 


        if nums == []: #handle corner cases 
            return [-1,-1]
        
        if len(nums) == 1: #corner cases 
            return [0,0] if nums[0] == target else [-1,-1]
        
        
        
        min = 0
        max = len(nums) 
        while min < max:  
            guess =  int((min + max)/2)
            print(guess)
            if nums[guess] >= target: #if greater, must be on the left
                max = guess  #also, if equal, may be another one on left 
            else:
                min = guess + 1  #why +1 ? because round down , baised towards the left 
                 
        lo = min #keep track of this left index 
        
        if min == len(nums) or nums[min] != target:   #if out of bound 
            return [-1,-1]

        
        min = 0
        max = len(nums)    
        while min < max:  
            guess =  int((min + max)/2) 
            if nums[guess] > target:  #if equal, maybe another one on right , so need to move min rather than max 
                max = guess 
            else:
                min = guess + 1 
                           
        return [lo,min-1]
    
    
