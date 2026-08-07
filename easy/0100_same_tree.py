from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return ((self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)))

solution = Solution()

# Example 1:
#     1          1
#    / \        / \
#   2   3      2   3
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Example 1:", solution.isSameTree(p1, q1))

# Example 2:
#     1          1
#    /            \
#   2              2
p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))
print("Example 2:", solution.isSameTree(p2, q2))

# Example 3:
#     1          1
#    / \        / \
#   2   1      1   2
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
print("Example 3:", solution.isSameTree(p3, q3))