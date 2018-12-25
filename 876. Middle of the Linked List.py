# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head 
        counter = 1 #because already counted the head 
        while curr.next:
            curr = curr.next
            counter = counter + 1
        
        middle = counter //2 + 1 
        #ie, when 6, middle = 4
        #when 5, middle = 3
        #handles both odd and even 
        
        curr = head
        while middle > 1: 
            curr = curr.next
            middle = middle - 1

        return curr
        
            
            
        
