class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result

    # 也可以迭代，用栈（stack）
    def postorderTraversalIterative(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]


# Test
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)

solution = Solution()
print(solution.postorderTraversal(root))
print(solution.postorderTraversalIterative(root))