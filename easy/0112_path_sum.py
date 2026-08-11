from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,current_sum):
            if node == None:
                return False
            current_sum+=node.val
            if node.left == None and node.right == None:
                return current_sum == targetSum
            left = dfs(node.left,current_sum)
            right = dfs(node.right,current_sum)
            return left or right
        return dfs(root,0)

solution = Solution()
# Example 1:
#          5
#         / \
#        4   8
#       /   / \
#      11  13  4
#     / \       \
#    7   2       1
# targetSum = 22

root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)

root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)

root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.right = TreeNode(1)

print(solution.hasPathSum(root1, 22))

# Example 2:
#      1
#     / \
#    2   3
# targetSum = 5

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(solution.hasPathSum(root2, 5))

# Example 3: Empty tree

root3 = None

print(solution.hasPathSum(root3, 0))