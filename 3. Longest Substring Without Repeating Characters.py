class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #eg, input = "abbca"
        #iterate through abbca, bbca, bca, ca,a  
        #everytime keep track of the index of starting position and the length of the non-repeating string starting from that index location
        #eg, {abbca:2,bbca:1,bca:3,ca:2,a:1}
        
        
        if s == "":
            return 0
        
        keeptrack = {}
    
        for i in range(len(s)):
            dictionary = {}
            counter = 0
            for letter in s[i:]:
                dictionary[letter] = dictionary.get(letter,0) + 1
                counter = counter + 1
                if dictionary[letter] == 2:
                    counter  = counter - 1 #if repeating ,this means the length of 1 minus of what we have reached at this point
                    break 
            
            keeptrack[i]  = counter

        return max(keeptrack.values())

    
    
    
    
    
   



#sliding window approach 
#this means iterating the string only once ,without double for loop
#if duplication occur, change starting position to the first occurence of that letter + 1 and use that as a new starting point for calculating the length 


#Need 3 temporary variables to find the longest substring: start, maxLength, and usedChars.

#Start by walking through string of characters, one at a time.
#Check if the current character is in the usedChars map, this would mean we have already seen it and have stored it's corresponding index.
#If it's in there and the start index is <= that index, update start to the last seen duplicate's index+1. This will put the start index at just past the current value's last seen duplicate. This allows us to have the longest possible substring that does not contain duplicates.

#If it's not in the usedChars map, we can calculate the longest substring seen so far. Just take the current index minus the start index. If that value is longer than maxLength, set maxLength to it.
#Finally, update the usedChars map to contain the current value that we just finished processing.



    def lengthOfLongestSubstring(self, s):
        maxlength = 0
        start = 0       
        letterseen = {}
        
        for i in range(len(s)):
            if s[i] in letterseen.keys() and start <= letterseen[s[i]]: #because initially we start at 0 , but now there is a duplication at a position greater than the start, so the current session becomes invalid, need to update the start location 
                start = letterseen[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1) 
                    
            letterseen[s[i]] = i
            
        return maxlength
                
        
    
    
    
        #abbca 
        
        #checking a (have seen nothing )
        #if a in usedChar and start<= usedChar[a] :
        
        #else
        #maxlength = max(0, 0 - 0 + 1)
        #maxlength = 1
        
        #usedChar[a] = 0
        
        #longest substring so far: a, becaused have only checked a
        
        
        
        
        
        
        
        #checking b (have seen a)
        #if b in usedchar..
        #else
        #maxlength = max(1, 1- 0 + 1)
        #maxlength = 2 
        
        #usedChar[b] = 1
        
        #longest substring so far: ab, because have only checked ab
        
        
        
        
        
        
        
        #checking b (have seen ab)
        #if b in usedchar and start <= usedChar[b] (and 0 <= 1) 
        #the start is less than , because initially we start at 0 , but now there is a duplication, so the string is invalid, so need to update the start location 
        #we know it is invalid, because the start is less than the location of duplication 
        
        #start = usedChar[b] + 1
        #start = 2 
        
        #we have seen b before, previously the location of b is 1, now start at 2, this allows us to get to a new string position that does not contain the duplicate of b
        
        
        
        
        
        
        #checking c (have seen abb) 
        #if c in usedChar.. 
        #else
        #maxLength = max(maxLength, i - start + 1)
        #maxlength = max(2, 3 - 2 + 1)
        #maxlength = 2
        
        #the current location is 3, but previously there is a duplication of length 2, so now the new substring with no duplication has length 2 
        
        
        
       
    
    
        
        #checking a (have seen abbc ) 
         #if a is in usedChar and start <= usedChar[a] (and 2<=0)
            #the start is not less than , because initially we start at 2, we see a duplication at 0 
            #this means last time a appears at location 0, it is meant for the last substring checking session 
            #not for the current duplication substring checking session 
            
        #so else 
        #maxLength = max(maxLength, i - start + 1)
        #maxlength = max(2, 4 - 2 + 1)
        #maxlength = 3
        
        #this means, here the location is at 4, last time we start at 2 (ie, this current duplication checking session starts at 2), so between location 4 and location 2, there are 3 characters 
        
        
        
        
        
        
        
        
        
        #abbbc
        
        #first check a
        #start = 0,
        #maxlength = 1 (because a) 
        
        #check b
        #start = 0
        #maxlength = 2 (ab)
        
        #check b
        #now duplication , and 0 < 2 
        #update start to 2 (ie, start new checking session at location 2 (last time b appear at 1, so add 1 to that ))
        
        #check b
        #now duplication, and 2 < 3
        #update start to 3 (start new checking session at location 3 (last time b appear at 2, add 1 to that))
        
        #check c
        #start = 3
        #max length :
        #c appear at 4, the previous valid checking session start at 3
        #so max length 2
        
        
        
        
        #abcda1234567    
        
        #check a 
        #start 0 
        #max length (0 - 0 + 1)
        
        #.....
    
        #check d
        #max length 4 so far 
        #(3 - 0 + 1)
        
        #check a 
        #duplication
        #start becomes 1 (because last time we see a appearing at 0, add 1 to that)
        
        #check 1
        #max length 5
        #(index - start + 1)
        #(5 - 1 + 1)
        
        
        
        
        
        #abbcaa  

        
        
        
        
        
        
                
                
