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

# DSA Problem: Sliding Window Logic Refinement
# Key Corrections & Observations:
# Initial Edge Case: My first mistake was omitting the length check at the very beginning (e.g., if s1.length > s2.length, return false).
# Final Window Validation: The second mistake was forgetting to add a final validation to check if the character counts match the window size after the loop terminates.
# The "Off-by-One" Logic: This is necessary because once the index reaches the end of the string, the final window is processed, but the comparison step might be skipped if it's only inside the loop. Without this final check, you miss the last possible permutation at the string's boundary.
# Revised Execution Flow:
# Edge Case Construction: Initialize by checking the lengths of both strings.
# Variable Initialization: Set up your frequency maps for both strings based on the length of the first string.
# Initial Window: Loop through the window size of the first string to populate the initial frequency maps.
# Sliding Window Loop:
# Identify the character to be added (leading edge) and the character to be removed (trailing edge).
# Perform the increment/decrement operations on the map.
# Cleanup: Delete keys with zero counts to keep the map size redundant-free.
# Comparison: Check if the current window's frequency map matches the target map.
# Final Boundary Check: Perform one last comparison after the loop to account for the final window.