class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
        return slow

solution = Solution()
print(solution.removeElement([3,2,2,3],3))
print(solution.removeElement([0,1,2,2,3,0,4,2],2))