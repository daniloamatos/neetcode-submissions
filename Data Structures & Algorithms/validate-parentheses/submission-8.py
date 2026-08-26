class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False

        symbols = {'(': ')', '[': ']', '{': '}'}
        stack = [] 
        for i in s:
            if i in symbols:
                stack.append(i)
            elif stack and i == symbols[stack[-1]]:
                stack.pop()
            else:
                return False

        return not stack