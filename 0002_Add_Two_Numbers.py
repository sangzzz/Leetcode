# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        l4 = l3
        x = ""
        y = ""
        while l1 != None:
            x = str(l1.val) + x
            l1 = l1.next
        while l2 != None:
            y = str(l2.val) + y
            l2 = l2.next
        X = int(x)
        Y = int(y)
        res = X + Y
        while res > 0:
            l3.val = res % 10
            res = res//10
            if res == 0:
                break
            l3.next = ListNode()
            l3 = l3.next

        return l4
