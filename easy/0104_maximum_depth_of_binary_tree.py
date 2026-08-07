from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left,right)+1
        return dfs(root)

# Example 1
#
#         3
#       /   \
#      9     20
#           /  \
#          15   7
root1 = TreeNode(
    3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)
print(Solution().maxDepth(root1))

# Example 2
#
#     1
#      \
#       2
root2 = TreeNode(
    1,
    None,
    TreeNode(2)
)
print(Solution().maxDepth(root2))