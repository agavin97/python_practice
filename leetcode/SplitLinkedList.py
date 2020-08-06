# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ret = []
        
        # Get length of list
        list_len = 0
        itr = root
        while itr != None:
            itr = itr.next
            list_len += 1
            
        # Items per box, items leftover
        num_items = list_len // k
        num_leftover = list_len % k
        
        i = 0
        itr = root
        while itr != None and i < k:
            head = itr
            
            for j in range(num_items - 1):
                itr = itr.next
            
            if num_leftover > 0 and num_items != 0:
                itr = itr.next
                num_leftover -= 1
                
            prev = itr
            itr = itr.next
            prev.next = None
                
            ret.append(head)
            i += 1
            
        # None fill any remaining boxes
        if i < k:
            while i < k:
                ret.append(None)
                i += 1
            
        return ret
