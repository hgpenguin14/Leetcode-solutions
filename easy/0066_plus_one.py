class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)-1
        while n>=0:
            if digits[n]!=9:
                digits[n]+=1
                return digits
            digits[n]=0
            n-=1
        if digits[0] == 0:
            return [1]+digits
        return digits

solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([9]))