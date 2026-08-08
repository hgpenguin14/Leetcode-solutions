from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# Example 1
# Input:
# nums = [-10, -3, 0, 5, 9]
# One possible output tree:
#          0
#        /   \
#      -3     9
#      /     /
#    -10    5
solution = Solution()
nums1 = [-10, -3, 0, 5, 9]
root1 = solution.sortedArrayToBST(nums1)

# Example 2
# Input:
# nums = [1, 3]
# With this implementation:
#      3
#     /
#    1
# Another valid answer could also be:
#    1
#     \
#      3
nums2 = [1, 3]
root2 = solution.sortedArrayToBST(nums2)