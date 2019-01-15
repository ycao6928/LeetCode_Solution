

class Solution:
    
    
    #approach 1: backtracking
    #we try every single jump pattern that takes us from the first position to the last. We start from the first position and jump to every index that is reachable. We repeat the process until last index is reached. When stuck, backtrack.

    def canJumpFromPosition(self, position, nums):
        if (position == len(nums) - 1 ):
            return True
        
        furthest = min(position + nums[position], len(nums) - 1)
        
        for nextposition in range(position+1, furthest):
            if (canJumpFromPosition(nextposition,nums)== True):
                return True
        
    def canJump(nums):
        return canJumpFromPosition(0, nums)
    
    
    
    #approach 2:
    #solve it as a graph problem
    #using dfs 
    
    def canJump(self, nums):

        visited , stack = set(), [0]
        
        while stack:
            position = stack.pop()
            print(position)
            if position >= len(nums) - 1 :
                return True 
            
            maxposition = min(position + nums[position], len(nums)-1)

 
            for i in range(position+1, maxposition+1):
                if i not in visited:
                    visited.add(i)
                    stack.append(i)
                
        return False

    
    
    
