class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case handling
        if not s or not t:
            return ""
        #
        count_t,window_map = {},{}

        #this creates the hashmap for the freq of t
        for i in range(len(t)):
            count_t[t[i]] = 1 + count_t.get(t[i],0)
        needed = len(count_t) #wrong cuz len(t) has dups
        have = 0
        res = [-1,-1] #not 0,0 cuz slice right is non inclusive
        reslen = float("inf")
        l = 0
        #sliding window 
        for r in range(len(s)):
            cur_char = s[r]
            window_map[cur_char] = 1 + window_map.get(cur_char,0) #increases the size of the window

            if cur_char in count_t and count_t[cur_char] == window_map[cur_char]:#cur_char in count_t very imp
                have +=1
            #this means we have all the charecter we need in this window
            #so we update res and try to shirnk the window
            while have == needed: #if onnly check once you need to shrink the window multiple times to check
                if (r-l+1)< reslen:
                    res = [l,r]
                    reslen = r-l+1
                #char to remove to shrink window
                char_removed = s[l]
                window_map[char_removed] -=1 
                if char_removed in count_t and window_map[char_removed] < count_t[char_removed]:# char_removed in count_t very imp
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen < float("inf") else ""             