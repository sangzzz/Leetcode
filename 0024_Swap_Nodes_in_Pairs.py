# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(l):
            if l == None or l.next == None:
                return 0
            t = l.val
            l.val = l.next.val
            l.next.val = t
            x = swap(l.next.next)
            return 1
        x = swap(head)
        return head
