# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def count(x):
            if x == None:
                return None
            val = x.val
            while x != None and val == x.val:
                x = x.next
            return x

        if head == None:
            return head
        root = head
        while head != None:
            ptr = count(head)
            head.next = ptr
            head = head.next
        return root
