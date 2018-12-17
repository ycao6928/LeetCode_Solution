# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

      
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        #if one of the linked list is empty, return the other list 
        if l1 is None:
            return l2
        if l2 is None:
            return l1    
        
        cur1 = l1
        cur2 = l2
        header = dummy = ListNode(0)
        
        #when both are not None 
        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val: 
                dummy.next = cur1 
                cur1 = cur1.next
            else:
                dummy.next = cur2
                cur2 = cur2.next
            dummy = dummy.next
            
#eg, [2,3] and [1,6]
#compare 2 and 1
#2 is larger
#dummy becomes 1


#[2,3] and [6]
#compare 2 and 6
#2 is smaller
#dummy becomes  1,2

#ie, attach whichever is smaller to the new list 

# and remember to move the cursor to the next
#ie, after attaching l1 to the dummy, need to do l1 = l1.next 
#after attaching l2 to the dummy, need to do l2 = l2.next

#also, in the end, need to do dummy = dummy.next

        while cur1 is not None:
            dummy.next = cur1
            cur1 = cur1.next
            dummy = dummy.next

        while cur2 is not None:
            dummy.next = cur2
            cur2 = cur2.next
            dummy = dummy.next
            
        return header.next

#when gets to the end , one list may becomes empty
# [] and [2,3,5]
#so if the list is empty, just attach everything to the new list 

      
        
        
        
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = header = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        dummy.next = l1 or l2 
        
#a smarter way  of handling one list empty 
#for whichever list that is not null, attach that to the new list 
        
        return header.next
    

  
