class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []
    
        dict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'], '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        if len(digits) == 1:
            return dict[digits]

        
        temp = dict[digits[0]]

        for i in range(1,len(digits)):
            holder = []
            thismultiply = dict[digits[i]]
            
            for s in temp:
                for j in thismultiply:
                    holder.append(s+j)

            temp = holder 
            
        return temp

    
    #eg, for the digit 234,
    #first set temp = a b c
    
    #then get the next thing to multiply on, ie, d e f
    
    #do the double for loop
    #keep the result in a holder array , which is set to be empty at the start of each iteration 
    
    #now set temp to be the result
    #ie, now temp becomes ad, ae, af ... and it gets multiplied with g h i
    
            
