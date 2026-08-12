class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result^=num
        return result

solution = Solution()
print(solution.singleNumber([2,2,1]))
print(solution.singleNumber([4,1,2,1,2]))
print(solution.singleNumber([1]))