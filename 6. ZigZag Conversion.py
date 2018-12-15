class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        #actually, no need to care about keeping the zigzag shape, 
        #because when reading, just reading across each row
        #so no need to have a 2D matrix with each number going into its correct/exact place 
        
        if numRows == 1: 
            return s
        
        
        rows = [''] * numRows

        num = (numRows-1)*2
        for i, item in enumerate(s):
            aftermod = i%num
            if aftermod >= numRows:
                rows[(numRows-1 - (aftermod-(numRows-1)))] += item
            else:
                rows[aftermod] += item
        return ''.join(rows) 
    
    
#eg,
#number of row = 5
#row 
#0    0           8
#1    1        7  9
#2    2     6     10
#3    3  5        11
#4    4           12

#first mod everything by  (number of row - 1 )*2 = 8
#0    0           0
#1    1        7  1
#2    2     6     2
#3    3  5        3
#4    4           4

#then, if the mod number is less than number of rows (ie, 5), then just add to the row directly
#ie, the 0  - 4, goes to the row number 0 - 4 , no need to do anything extra

#but for the number or equal to the number of rows , need to do further computation
#ie, for the number 5 , 6, 7
#first compute number of row - 1 = 4
#then 
# 5 - 4 = 1
# 4 - 1  =3
#so 5 goes to row 3

# 6 - 4 = 2
# 4 - 2 = 2 

# 7 - 4  = 3
# 4 - 3 = 1
