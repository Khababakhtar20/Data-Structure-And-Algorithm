# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node):
            nonlocal diameter
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return diameter
