# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy  = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        
        while prev.next:
            curr = prev.next
            
            if curr.next and curr.val == curr.next.val:
                dupvalue = curr.val
                while curr.next and curr.next.val == dupvalue:
                    curr = curr.next
                prev.next = curr.next
               
            else:
                prev = prev.next
                
        return dummy.next
    
    
    
    
    
    -1 ->   1 ->    1 ->    1 ->  3 -> 5
    prev  curr curr.next
    
    keep a prev pointer (which we need to link it to the next non - duplication node)
    
    start checking from prev
    if next one has the same number, then write down this number
    keep going to the next one and checking if the next one has the same number
    
    Stop when the next one does not have same number 
     -1 ->   1 ->    1 ->    1 ->  3     -> 5
    prev                  curr   curr.next    
                     
    Link the prev to the curr.next
     -1 ->   3         -> 5 
    prev    curr.next
    
    
    start searching from prev again 
    -1 ->   3    -> 5
    prev    curr
    
    the next value is not the same 
    so prev = prev.next
    curr = prev.next
    
    -1 ->   3      -> 5
            prev      curr
    
    not the same, so prev = prev.next
     -1 ->   3      -> 5
                       prev   
        
    there is no more prev.next
    terminate 
    
    
    
    
    
                
