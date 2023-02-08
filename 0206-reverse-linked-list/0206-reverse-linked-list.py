class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = None
    
        while head:
            next_node = head.next
            head.next = dummy
            dummy = head
            head = next_node
        return dummy
            
            
        
        