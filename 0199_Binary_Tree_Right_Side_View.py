# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        T = {}
        def traverse(level, node):
            if not node:
                return True
            T[level] = node.val
            traverse(level+1, node.left)
            traverse(level+1, node.right)
        traverse(1, root)
        return list(T.values())