# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        heap = []
        heapq.heapify(heap)
        
        
        new_list = dummy
        
        
        for i in range(len(lists)):
            if lists[i]:

                a = [lists[i].val,i]
                heapq.heappush(heap, a)
            
        while heap:
            curr, i = heapq.heappop(heap)
            dummy.next = ListNode(curr)
            dummy = dummy.next
        
            if lists[i].next:
                lists[i] = lists[i].next 
                heapq.heappush(heap, [lists[i].val, i])
                
            
        return new_list.next
            
            
            
        