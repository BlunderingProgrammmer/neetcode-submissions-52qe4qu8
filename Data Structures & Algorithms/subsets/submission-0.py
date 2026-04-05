class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        #pass in the iterator
        def dfs(i):
            if i >=len(nums):
                res.append(subset.copy())
                return

            #represents the branch to include element in subset
            subset.append(nums[i])
            dfs(i+1)

            #represent the step to include empty list instead elements
            subset.pop()
            dfs(i+1)
        #initialize using 0 index 
        
        dfs(0)
        return res