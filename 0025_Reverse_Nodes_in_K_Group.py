# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(l):
            if l == None:
                return 0
            else:
                x = l
                n = 1
                nodes = [x.val]
                while n < k:
                    x = x.next
                    if x == None:
                        break
                    nodes.append(x.val)
                    n += 1
                if n != k:
                    return 0
                for i in nodes[::-1]:
                    l.val = i
                    l = l.next
                return reverse(l)
        x = reverse(head)
        return head
