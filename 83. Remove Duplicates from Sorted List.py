class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """    
# input list is sorted, so can comparing its value to the node after it in the list. 
# If same value, we change the next pointer of the current node to the one after the next node.

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head
