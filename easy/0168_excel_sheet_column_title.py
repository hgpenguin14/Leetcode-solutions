class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        char = ""
        while columnNumber>0:
            columnNumber-=1
            a = columnNumber%26
            b = columnNumber//26
            result.append(chr(ord('A') + a))
            columnNumber = b
        return ''.join(result[::-1])

solution = Solution()
print(solution.convertToTitle(1))
print(solution.convertToTitle(28))
print(solution.convertToTitle(701))