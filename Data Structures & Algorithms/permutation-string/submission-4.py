class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:     
        if len(s1) > len(s2):
            return False   
        count_s1 = {}
        window_size_on_s2 = {}

        #intialize map freq for both
        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i],0)
            window_size_on_s2[s2[i]] = 1 + window_size_on_s2.get(s2[i],0)

        #comparision 
        for j in range(len(s2)-len(s1)):
            if count_s1 == window_size_on_s2:
                return True

            #get the next char to be compared/added/removed
            char_to_be_added = s2[j+len(s1)] # j points to the leftmost in the window so len(s1) takes to next char
            char_to_be_removed = s2[j] 

            window_size_on_s2[char_to_be_added] = 1 + window_size_on_s2.get(char_to_be_added,0)
            window_size_on_s2[char_to_be_removed] -= 1 # cant set directly to zero if you doo then if there are 
            #multiple of the same then it will remove all of them
            if window_size_on_s2[char_to_be_removed] == 0:
                del window_size_on_s2[char_to_be_removed] 
            
        return count_s1 == window_size_on_s2