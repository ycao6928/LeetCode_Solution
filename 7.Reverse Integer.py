class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = str(x)
        
        #if negative, remove the negative sign
        if x < 0:
            tmp = tmp[1:]
            
        tmp = tmp[::-1]
        tmp = int(tmp)
        
        if x < 0:
            tmp *= -1
        
        #check for overflow 
        if tmp > pow(2,31)-1 or tmp < pow((-2),31):
            tmp = 0
            
        return tmp
