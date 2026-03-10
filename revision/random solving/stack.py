class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {'{':'}','[' : ']','(':')'}
        stack = []
        for ch in s:
            if ch in '{[(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if mappings[stack[-1]] != ch:
                    return False
                stack.pop()
        return not stack


sol = Solution()
print(sol.isValid("()[]{}"))


