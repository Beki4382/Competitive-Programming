# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_set = set()
        curr = head
        
        while curr:
            
            if curr in node_set:
                return curr
            node_set.add(curr)
            curr = curr.next
            
        return 
        