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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        return self.divide_and_conquer(root)

    def traverser(self, root):
        output = []
        self.preorderHelper(root, output)
        return output

    def preorderHelper(self, root, output):
        if root is None:
            return
        output.append(root.val)
        self.preorderHelper(root.left, output)
        self.preorderHelper(root.right, output)

    def divide_and_conquer(self, root):
        output = []
        if root is None:
            return output
        output.append(root.val)
        left = self.divide_and_conquer(root.left)
        right = self.divide_and_conquer(root.right)
        return output + left + right
