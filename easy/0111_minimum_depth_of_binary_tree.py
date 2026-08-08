from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            if left == 0:
                return right+1
            if right == 0:
                return left+1
            return min(left,right)+1
        return dfs(root)

solution = Solution()
# Example 1
# Tree:
#          3
#        /   \
#       9     20
#            /  \
#           15   7
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.minDepth(root1))

# Example 2
# Tree:
#       2
#        \
#         3
#          \
#           4
#            \
#             5
#              \
#               6

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(solution.minDepth(root2))