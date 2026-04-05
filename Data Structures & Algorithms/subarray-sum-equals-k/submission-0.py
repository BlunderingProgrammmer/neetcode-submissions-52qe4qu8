class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 # u are returning no subrarry possible not the exact subarray 
        prefix_count_hash = {0:1} #base case - the number 0 has a count of 1 def case
        
        cursum = 0
        for i in nums:
            cursum += i
            target_to_search_hash = cursum -k # give the diff or saved prefix sum to look for  
            
            if target_to_search_hash in prefix_count_hash:
                res += prefix_count_hash[target_to_search_hash]
            # in the hash u are saving the cur sum anot the ideal target
            prefix_count_hash[cursum] = 1 + prefix_count_hash.get(cursum,0)
        return res
