"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        return self.minDepthHelper(root)

    def minDepthHelper(self, root):
        if root is None:
            import sys
            return sys.maxint
        if root.left is None and root.right is None:
            return 1
        left_depth = self.minDepthHelper(root.left)
        right_depth = self.minDepthHelper(root.right)
        min_depth = min(left_depth, right_depth) + 1
        return min_depth
