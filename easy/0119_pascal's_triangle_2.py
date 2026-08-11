class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            row.append(1)
            for j in range(i-1,0,-1):
                row[j] = row[j-1]+row[j]
        return row

solution = Solution()
# Example 1:
# rowIndex = 3
#       1
#      1 1
#     1 2 1
#    1 3 3 1

print(solution.getRow(3))

# Example 2:
# rowIndex = 0

print(solution.getRow(0))

# Example 3:
# rowIndex = 1

print(solution.getRow(1))