# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return None
        curr = head
        sz = 0
        while curr is not None:
            sz+=1
            curr = curr.next
        if sz < n:
            return None
        curr = head
        delete_pos = sz-n+1
        if delete_pos==1:
            head = head.next
            return head
        for i in range(1, delete_pos):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        del curr

        return head
        
        