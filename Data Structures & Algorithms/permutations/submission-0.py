class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        for n in nums:
            new_perms = []
            for p in perm:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perm = new_perms
        return perm