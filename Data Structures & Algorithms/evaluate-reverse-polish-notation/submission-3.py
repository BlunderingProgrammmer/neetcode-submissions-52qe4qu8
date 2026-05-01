class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                a,b = stack.pop(),stack.pop()
                result =  a+b
                stack.append(result)
            elif char == "-":
                a,b = stack.pop(),stack.pop()
                result =  b-a
                stack.append(result)
            elif char == "*":
                a,b = stack.pop(),stack.pop()
                result =  a*b
                stack.append(result)
            elif char == "/":
                a,b = stack.pop(),stack.pop()
                result =  int(b/a)
                stack.append(result)
            else:
                stack.append(int(char))
        return stack[0] 