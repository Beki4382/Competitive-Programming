# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # method one ----> using two pointers(no need for extra space o(1)) 
        
        slow, fast = head, head
        
    
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        
        return False
     
        
        
        # method two -----> using hash set to get seen nodes o(n)
#         node_set = set()
        
#         curr = head
#         while curr:
#             if curr in node_set:
#                 return True
            
#             node_set.add(curr)
#             curr = curr.next
#         return False
            
                
        