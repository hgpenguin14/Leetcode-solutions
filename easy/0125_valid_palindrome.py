class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned+=char
        return cleaned == cleaned[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))