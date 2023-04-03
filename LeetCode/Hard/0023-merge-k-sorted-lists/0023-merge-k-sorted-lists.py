# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = cur = ListNode(None)
        min_heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
            
        while min_heap:
            node = heapq.heappop(min_heap)
            i, cur.next = node[1], node[2]
            
            cur = cur.next
            if cur.next:
                heapq.heappush(min_heap,(cur.next.val, i, cur.next))
                
        return root.next
            