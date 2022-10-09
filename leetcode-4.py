# Leetcode assignment #4
# 94. Binary Tree Inorder Traversal
# Submitted 6 Oct 2022

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base case
        if root == None:
            return []
        
        traversal = []
        
        # Traverse left
        traversal.extend(self.inorderTraversal(root.left))
        # Traverse node
        traversal.append(root.val)
        # Traverse right
        traversal.extend(self.inorderTraversal(root.right))
        
        return traversal
