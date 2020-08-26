# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        head = ListNode()
        flag = 0
        nodes = []
        while flag == 0:
            if l1.val < l2.val:
                ptr = ListNode(l1.val, None)
                l1 = l1.next
            else:
                ptr = ListNode(l2.val, None)
                l2 = l2.next
            nodes.append(ptr)
            if l1 == None:
                flag = 1
            elif l2 == None:
                flag = 2

        head = nodes[0]
        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]
        if flag == 1:
            nodes[-1].next = l2
        elif flag == 2:
            nodes[-1].next = l1

        return head
