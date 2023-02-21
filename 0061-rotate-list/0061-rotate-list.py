# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr = head
        count = 1
        
        while curr.next:
            count += 1
            curr = curr.next
            
        curr.next = head
        
        k = count - (k%count)
        
        temp = head
        while k > 1:
            temp = temp.next
            k -= 1
            
        new_head = temp.next
        temp.next = None
        
        return new_head