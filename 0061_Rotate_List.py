# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        elems = []
        if head == None:
            return head
        i = head
        while i != None:
            elems.append(i.val)
            i = i.next
        k %= len(elems)
        elems = elems[-k:] + elems[0:-k]
        # print(elems)
        i = head
        j = 0
        while i != None:
            i.val = elems[j]
            i = i.next
            j += 1
        return head
