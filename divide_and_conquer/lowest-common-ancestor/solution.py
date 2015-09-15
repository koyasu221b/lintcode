"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None or root is A or root is B:
            return root

        left_ancestor = self.lowestCommonAncestor(root.left, A, B)
        right_ancestor = self.lowestCommonAncestor(root.right, A, B)
        if left_ancestor is not None and right_ancestor is not None:
            return root

        if left_ancestor is not None:
            return left_ancestor

        if right_ancestor is not None:
            return right_ancestor

        return None
