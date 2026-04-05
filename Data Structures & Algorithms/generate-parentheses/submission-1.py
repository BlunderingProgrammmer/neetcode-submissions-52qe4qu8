class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtracking(openn,closedn):
            if n == openn == closedn:
                res.append(''.join(stack)) #base case 
                return res
            if openn < n:
                stack.append('(')#consider as each  recursive call as clone with updated values from prev run
                backtracking(openn+1,closedn)
                stack.pop()
            if closedn < openn:
                stack.append(')')
                backtracking(openn,closedn+1)
                stack.pop()
        backtracking(0,0)
        return res