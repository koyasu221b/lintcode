# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        # find the target node
        current = self.find_current_node(root,p)
        if current is None:
            return None
        # node has right child
        if current.right is not None:
            current = current.right
            while current.left is not None:
                current = current.left
            return current

        # node has no right child
        else:
            ancestor = root
            successor = None
            while ancestor.val != current.val :
                if ancestor.val > current.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor

    def find_current_node(self, root,p):
        current = root
        while current is not None and current.val != p.val:
            if p.val == current.val:
                return current
            elif p.val > current.val:
                current = current.right
            else:
                current = current.left
        return current
