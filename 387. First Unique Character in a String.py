class Solution:
    
    
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dictionary  = {}
        #if the key does not exist, return 0 as default, then add 1 
        #if the key exists, add 1 
        for letter in s:
            dictionary[letter] = dictionary.get(letter, 0) + 1
            
            
        for letter in s:
            if dictionary[letter]==1:
                return s.find(letter) #the s.find() finds the index of a char in a string 
        return -1 
 



    def firstUniqChar(self, s):
        dictionary = collections.Counter(s)     #can be solved naturally using counter 

        for index, letter in enumerate(s):
            if dictionary[letter]==1:
                return index
            
        return -1
