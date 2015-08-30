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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        balanced, max_depth = self.isBalanced_helper(root)
        return balanced


    def isBalanced_helper(self, root):
        if root is None:
            return True, 0

        is_left_balanced, left_depth = self.isBalanced_helper(root.left)
        if not is_left_balanced:
            return is_left_balanced, left_depth
        is_right_balanced, right_depth = self.isBalanced_helper(root.right)
        if not is_right_balanced:
            return is_right_balanced, right_depth

        diff = abs(left_depth - right_depth)
        return diff <=1, max(left_depth, right_depth)+1
