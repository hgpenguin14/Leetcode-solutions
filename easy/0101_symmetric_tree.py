from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            return(isMirror(left.left,right.right) and isMirror(left.right,right.left))
        return isMirror(root.left, root.right)

# Example 1
#
#         1
#       /   \
#      2     2
#     / \   / \
#    3  4  4  3
root1 = TreeNode(
    1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3))
)
print(Solution().isSymmetric(root1))

# Example 2
#
#         1
#       /   \
#      2     2
#       \     \
#        3     3
root2 = TreeNode(
    1,
    TreeNode(2, None, TreeNode(3)),
    TreeNode(2, None, TreeNode(3))
)
print(Solution().isSymmetric(root2))