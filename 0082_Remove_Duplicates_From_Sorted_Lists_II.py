# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head
        if root == None:
            return root

        def count(x):
            cnt = 0
            if x == None:
                return 0, None
            val = x.val
            while x != None and x.val == val:
                cnt += 1
                x = x.next
            return cnt, x
        while True:
            x, ptr = count(root)
            if x >= 2:
                root = ptr
                head = ptr
            else:
                break
        if root == None:
            return root
        while head.next != None:
            x, ptr = count(head.next)
            if x >= 2:
                head.next = ptr
            else:
                head = head.next
        return root
