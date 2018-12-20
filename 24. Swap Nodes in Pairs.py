
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#这题为什么普遍都用Dummynode?
#Head的位置可能会变，比如 1 > 2 > Null , 之后会返回 2 > 1 > Null, head的位置从1变成了2


        dummy = ListNode(0)
        dummy.next  = head
        curr = dummy 
        

        
        while curr.next and curr.next.next: #only when there are two more nodes after the current node, do we get the next two nodes and swap their position 
            first = curr.next          
            second = curr.next.next 
        
            first.next = second.next  #looks like we are just switching 2 nodes 
            second.next = first      #but actually involves 3 nodes 
            curr.next = second

            curr = curr.next.next   #update current to the next starting position 


        return dummy.next
    
    
#note, why set first = curr.next at the start of the loop instead of at the end of the loop?
#if updating in the end after we have upadted the curr to the curr.next.next, will get null pointer exception
#if updating in the first line, the null pointer exception is already handled by the while loop condition 
