from queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i, l))
        while not q.empty():
            val, i, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, i, node))
        return head.next
