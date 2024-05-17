class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = {}
        window_counts = {}
        
        for c in s1:
            s1_counts[c] = s1_counts.get(c, 0) + 1
            
        goal = len(s1_counts)
        counts_met = 0
        
        #first len(s1) - 1 characters of s2, first iteration of loop will have right as the final letter
        for i in range(len(s1) - 1):
            window_counts[s2[i]] = window_counts.get(s2[i], 0) + 1
            
        for c in s1_counts:
            if window_counts.get(c, 0) == s1_counts[c]:
                counts_met += 1
            
        for i in range(len(s2) - len(s1) + 1):
            j = i + len(s1) - 1
            
            left = s2[i]
            right = s2[j]
            
            window_counts[right] = window_counts.get(right, 0) + 1
            if right in s1_counts and s1_counts[right] == window_counts[right]:
                #we can do this because window_counts[right] must change every iteration,
                #so if its equal now it wasn't equal in the previous iteration
                counts_met += 1
                
                if counts_met == goal:
                    return True
            elif right in s1_counts and s1_counts[right] == window_counts[right] - 1:
                #don't need to worry about other letters because sliding window only has enough space for
                #len(s1) letters and every letter must be in s1_counts, so all counts cannot be met if
                #another letter is in the window
                counts_met -= 1
            
            window_counts[left] -= 1
            
            if left in s1_counts and s1_counts[left] == window_counts[left]:     
                counts_met += 1
                
            elif left in s1_counts and s1_counts[left] == window_counts[left] + 1:
                counts_met -= 1
        
        return False
                
            
            