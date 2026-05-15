class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,cursum = 0,0
        prefixsum_freq_map = {0:1} # in an valid subarray nums ...0 occurs exactly once

        for n in nums:
            cursum+= n
            target_to_find = cursum - k # the element we are looking to chop off 

            if target_to_find in prefixsum_freq_map:
                res += prefixsum_freq_map[target_to_find]
            #above meaning we can chop off that num in freq ways
            prefixsum_freq_map[cursum] = 1 + prefixsum_freq_map.get(cursum,0)
        return res














































        # res = 0 # u are returning no subrarry possible not the exact subarray 
        # prefix_count_hash = {0:1} #base case - the number 0 has a count of 1 def case prefix_sum->freq of thAT SUM
        
        # cursum = 0
        # for i in nums:
        #     cursum += i
        #     target_to_search_hash = cursum -k # give the diff or saved prefix sum to look for  
            
        #     if target_to_search_hash in prefix_count_hash:
        #         res += prefix_count_hash[target_to_search_hash]
        #     # in the hash u are saving the cur sum anot the ideal target
        #     prefix_count_hash[cursum] = 1 + prefix_count_hash.get(cursum,0)
        # return res