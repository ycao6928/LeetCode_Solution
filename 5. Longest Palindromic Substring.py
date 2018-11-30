class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        p1 = ""

        #odd case , eg 'aba'
        #begin checking from 'a', then 'b', then 'aba'
        for i in range(len(s)):
            checkleft = i
            checkright = i
          
        #good way of checking the boundary
        #don't have to check the boundary as a separate if statement, because the while loop check each condition by order, so if index out of bound, the s[checkleft] won't be evaluated 
            while checkleft >=0 and checkright < len(s) and s[checkleft] == s[checkright]: 
                checkleft  = checkleft -1
                checkright = checkright + 1
                temp1 = s[checkleft+1:checkright] #grab the previous palindrome, the previous palindrome has index checkleft + 1,  and checkright - 1, but because the slicing index exclude the last index, so [checkleft+1, checkright]
            
            #if at this index, the palindrome is longer, then store this palindrome, and move on to check the next index 
            if len(temp1) > len(p1): 
                p1 = temp1



        #even case, eg,'acca'
        #begin checking from 'ac', then 'cc', then 'acca'
        for i in range(0,len(s)):
            checkleft = i
            checkright = i+1

            while checkleft >= 0 and checkright < len(s) and s[checkleft] == s[checkright]: 
                checkleft  = checkleft -1
                checkright = checkright + 1
                temp1 = s[checkleft+1:checkright]
            
            if len(temp1) > len(p1):
                p1 = temp1
        
        return p1
