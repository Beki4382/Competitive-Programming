# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        dummy = ListNode()
      
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        dummy = ListNode()
        res = None
        dummy.next = res
        carry = 0
        
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            
            new_node = ListNode(digit)
            new_node.next = res
            res = new_node
        if carry > 0:
            new_node = ListNode(carry)
            new_node.next = res
            res = new_node

            
        return res
            
            
            
        