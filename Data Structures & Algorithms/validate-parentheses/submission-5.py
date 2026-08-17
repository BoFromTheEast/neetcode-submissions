class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isValid = {'}':'{', ')': '(', ']': '['}

        for char in s:
            if char in isValid:
                if stack and stack[-1] == isValid[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True