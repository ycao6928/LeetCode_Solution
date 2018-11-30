# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #create a dummy node 
        #helpful when the linked list only has 2 elements
        #eg,linked list  is [1,2], counter can only go to 1, but need to remove the second element , need to have extra condition
        #if the linked list becomes [dummy, 1,2], now counter can go to 2, and becomes dummy.next = dummy. next . next
        #ie, becomes [dummy, 2], the 1 get successfully deleted 
        
        dummy = ListNode(0)
        dummy.next = head
        node = node2 = dummy
        
        counter = 0
        
        while node.next != None: 
            node = node.next
            counter = counter + 1
            if counter > n:
                node2 = node2.next
        
        node2.next = node2.next.next
        
        return dummy.next

    

     #this essentially keeps two pointer, the second pointer is n nodes behind the first pointer 
     #eg, [ 1,2,3,4,5], delete the 2nd last element (ie, delete 4 to become [1,2,3,5])
     #the first pointer reaches 5, sees there is no next node, gets out of the loop
     #at this time, the second pointer is at 3 (because it is 2 nodes behind the first pointer)
    #3.next = 3.next.next
    #this means 5 comes after 3 
    #so 4 gets deleted
    #the dummy.next gets returned, so return [1,2,3,5]
        
