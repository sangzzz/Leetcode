# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        elements = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            elements.append(node.val)
            inorder(node.right)
        inorder(root)
        sums = []
        sumOfElements = sum(elements)
        sums.append(sumOfElements)
        for i in range(1, len(elements)):
            sums.append(sums[-1] - elements[i-1])
        map = {}
        for i in range(len(elements)):
            map[elements[i]] = sums[i]
        def updateinorder(node):
            if not node: return node
            updateinorder(node.left)
            node.val = map[node.val]
            updateinorder(node.right)
        updateinorder(root)
        return root