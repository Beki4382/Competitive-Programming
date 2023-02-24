# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        max_sum  = 0
        
        for i in range(len(arr)):
            max_sum = max(max_sum, arr[i] + arr[(i+1) * -1])
            
        return max_sum    
        
        
        
        
        
        
#         if not head:
#             return head
#         slow = head
#         fast = head
        
#         while fast and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
        
       
#         new_head = slow.next
#         slow.next = None
        
#         prev = None
#         curr = new_head
#         while curr:
#             new_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = new_node
  
#         max_sum = 0
#         sum_ = 0
        
#         while head:
#             max_sum = max(max_sum, head.val + prev.val)
            
#             head.next
#             prev.next
#         return max_sum
            
        
            
       