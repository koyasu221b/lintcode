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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        return self.inorderHelper(root)

    def inorderHelper(self, root):
        if root is None:
            return []
        left = self.inorderHelper(root.left)
        right = self.inorderHelper(root.right)
        return left + [root.val] + right
