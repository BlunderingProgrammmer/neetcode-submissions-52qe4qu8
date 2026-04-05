class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in close_to_open:
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False