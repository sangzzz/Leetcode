# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def recurs(ptr, k):
            if ptr.next == None:
                return 0
            x = recurs(ptr.next, k) + 1
            if x == k:
                if x == 1:
                    ptr.next = None
                else:
                    ptr.next = ptr.next.next
            return x
        x = recurs(head, n)
        if x == n-1:
            head = head.next
        return head
