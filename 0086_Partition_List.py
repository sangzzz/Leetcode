# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return head
        elif head.next == None:
            return head
        great = []
        rootLess = ListNode()
        rearLess = rootLess
        rootGreat = ListNode()
        rearGreat = rootGreat
        while head != None:
            ptr = ListNode(head.val)
            if head.val < x:
                rearLess.next = ptr
                rearLess = ptr
            else:
                rearGreat.next = ptr
                rearGreat = ptr
            head = head.next
        rootLess, rootGreat = rootLess.next, rootGreat.next
        if not rootLess:
            return rootGreat
        rearLess.next = rootGreat
        return rootLess
