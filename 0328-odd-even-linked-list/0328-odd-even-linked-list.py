# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        odd = head
        
        if head is None:
            return head

        even = head.next
        odd_head = odd
        even_head = even
        
        
        while even and even.next != None:
            
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        odd.next = even_head
        
        return odd_head
        
        