class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = result[-1][j-1]+result[-1][j]
            result.append(row)
        return result

solution = Solution()
# Example 1:
# numRows = 5
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1

print(solution.generate(5))

# Example 2:
# numRows = 1

print(solution.generate(1))