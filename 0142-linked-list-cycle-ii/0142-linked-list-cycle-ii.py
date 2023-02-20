# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #method one -----> solve O(1)
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                p1 = head
                p2 = fast
                while p1:
                    if p1 == p2:
                        return p1
                    p1 = p1.next
                    p2 = p2.next
                    
        return 
        # method two ----> solve using hashset O(n)
        
#         node_set = set()
#         curr = head
        
#         while curr:
            
#             if curr in node_set:
#                 return curr
#             node_set.add(curr)
#             curr = curr.next
            
#         return 
        