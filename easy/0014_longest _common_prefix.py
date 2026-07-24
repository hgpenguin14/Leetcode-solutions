class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]
        for i in range(len(first)):
            char = first[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return first[:i]
        return first

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))