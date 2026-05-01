class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)#how -well you need output array of len temp
        stack = [] # pair of values temp,index
        for i,t in enumerate(temperatures):#current iteration of temp on the array ,also you need to calculate the distance between indesx
            while stack and t > stack[-1][0]:#check the top of the stack and the first value which is temp
                stackT,stack_index = stack.pop()#if true get the index and calc distance
                res[stack_index] = (i-stack_index)
            stack.append([t,i])
        return res
