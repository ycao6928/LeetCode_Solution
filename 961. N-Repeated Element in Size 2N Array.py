class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        c = collections.Counter(A) 
        return c.most_common(1)[0][0]
    

    #actually, no need to use a counter
    #why?
    #because only 1 element is repeating! 

    #so , just add number  1 by 1 into a list or something
    #if we see a repeating number 
    #just return this number immediately !
    
    
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        list = set()
        for thisone in A:
            if thisone not in list:
                list.add(thisone)
            else:
                return thisone
