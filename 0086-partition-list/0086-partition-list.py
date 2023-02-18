# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = lis1 = ListNode(0)
        head2 = lis2 = ListNode(0)
        
        while head:
            if head.val < x:
                lis1.next = head
                lis1 = lis1.next
            else:
                lis2.next = head
                lis2 = lis2.next
            head = head.next
            
        lis2.next = None
        lis1.next = head2.next
        
        return head1.next
        