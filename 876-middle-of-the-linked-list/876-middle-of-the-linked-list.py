class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        t ,h =head, head
        while h and h.next :
            t = t.next
            h = h.next.next
        return t
        