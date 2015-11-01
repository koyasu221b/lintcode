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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, root, result):
        if root is None:
            return
        self.traversal(root.left, result)
        self.traversal(root.right, result)
        result.append(root.val)

    def divide_and_conquer(self, root):
        if root is None:
            return []
        sub_result_left = self.divide_and_conquer(root.left)
        sub_result_right = self.divide_and_conquer(root.right)
        return sub_result_left+ sub_result_right  + [root.val]

