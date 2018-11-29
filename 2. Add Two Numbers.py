# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    #retrieve the numbers first, do addition, then construct the list 
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l2number = ""
        l1number = ""

        while l2.next != None: #while there are next node (the last node does not have next node)
            currentnum = l2.val #get the value 
            l2 = l2.next #go to the next node 
            l2number = l2number + str(currentnum) #ie, ""+2  = 2, "25"+3 = 253
        l2number = l2number + str(l2.val)   #the last node does not have next node, so loop does not get evaluated 
            
        while l1.next != None:
            currentnum = l1.val
            l1 = l1.next
            l1number = l1number + str(currentnum)
        l1number = l1number + str(l1.val)  
        
        
        
        l2number = l2number[::-1] #"253" becomes "352"
        l1number = l1number[::-1]
        sum = str(int(l2number) + int(l1number)) #add the two numbers 
        sum = sum[::-1] #reverse again 
            
        
        #construct the singly linked list 
        firstnode = ListNode(0)  #first create a dummy starter node 
        pointer = firstnode #called it as pointer 
        for i in sum: 
            pointer.next = ListNode(i) #create a node containing the value and link it at the next node 
            pointer = pointer.next #go to the next node 
            
        
        return firstnode.next      
    
    
    #construct on the run 
    def addTwoNumbers(self, l1, l2):
        carry = 0
        n = ListNode(0) #set a starter dummy node , with value 0 
        root = n #let this starter node by n 

        
        #while there are numbers to add 
        while l1 or l2 or carry: 
            current1 = current2 = 0 
            if l1: #if l1 is not None 
                current1 = l1.val #get the number  
                l1 = l1.next #go to the next number 
            if l2:
                current2 = l2.val
                l2 = l2.next
            carry, val = divmod(current1+current2+carry, 10)  #eg, 9 + 9 + 1 =19 
            #return quotient and remainder , eg, 19/10 gives carry = 1, remainder = 9
            #the 9 gets stored in the current node, the 1 get carried over by the loop 
            
            
            n.next = ListNode(val) #create a new node, link it as the next node 
            n = n.next #go to the next node 
        
        
        return root.next #return the next number after this dummy node 
        
        
    
