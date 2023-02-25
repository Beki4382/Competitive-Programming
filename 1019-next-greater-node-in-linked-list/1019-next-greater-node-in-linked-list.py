# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return head
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        n = len(arr)
        stack = []
        d = {}
        
        for i,val in enumerate(arr):
            if not stack:
                stack.append((i,val))
               
            else:
                while stack and val > stack[-1][1]:
                    d[stack.pop()] = val
                stack.append((i,val))
            
        output = [0]*n
        
            
        while stack:
            d[stack.pop()] = 0
       
        for v in d:
            output[v[0]] = d[v]
        
            
            
        
        
        return output 

        
            