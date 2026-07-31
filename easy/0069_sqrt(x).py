"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left = 0
        right = x
        while left<=right:
            mid = (left+right)//2
            if mid*mid>x:
                right = mid-1
            elif mid*mid==x:
                return mid
            else:
                left = mid+1
        return right

solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))