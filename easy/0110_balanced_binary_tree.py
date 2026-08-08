from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1:
                return -1
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root)!=-1

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

print(solution.isBalanced(root1))

# Example 2
# Tree:
#
#              1
#            /   \
#           2     2
#          / \
#         3   3
#        / \
#       4   4
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)

root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)

root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

print(solution.isBalanced(root2))

# Example 3
# Tree:
# Empty tree
root3 = None
print(solution.isBalanced(root3))