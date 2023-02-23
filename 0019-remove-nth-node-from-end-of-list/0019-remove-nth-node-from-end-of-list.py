# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head and head.next:
            return head
        
        curr = head
        prev = head
        
        while n > 0:
            curr = curr.next
            n -= 1
            
        if curr == None:
            return head.next
        
        while curr.next != None:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next
        
        return head