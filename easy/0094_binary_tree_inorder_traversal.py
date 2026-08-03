from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        traverse(root)
        return result

solution = Solution()

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print("Example 1:", solution.inorderTraversal(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)
print("Example 2:", solution.inorderTraversal(root2))

root3 = None
print("Example 3:", solution.inorderTraversal(root3))

root4 = TreeNode(1)
print("Example 4:", solution.inorderTraversal(root4))