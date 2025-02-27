# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge iteratively 
        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.merge_list(lists[i], lists[i + interval])
            interval = interval * 2
        return lists[0] if n > 0 else None



    def merge_list(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next
        

        return dummy.next
