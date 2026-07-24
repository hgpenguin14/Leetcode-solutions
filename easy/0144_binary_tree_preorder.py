class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if node is None:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

    # 迭代也可以，用栈（stack）
    def preorderTraversalIterative(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # 先放右，再放左
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


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
print(solution.preorderTraversal(root))
print(solution.preorderTraversalIterative(root))