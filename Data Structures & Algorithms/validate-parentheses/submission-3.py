class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {'}':'{',')':'(',']':'['}

        for char in s:
            if char in mapper and len(stack) > 0:
                if stack[-1] == mapper[char]:
                    stack.pop()
                else:
                    return False   
            else:
                stack.append(char)
                
        return True if len(stack) == 0 else False           
        