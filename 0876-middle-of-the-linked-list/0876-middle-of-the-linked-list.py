# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
            
        mid = length//2
        
        curr = head
        while mid:
            curr = curr.next
            mid -= 1
        return curr