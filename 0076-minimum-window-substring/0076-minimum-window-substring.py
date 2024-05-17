class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_counts = {char: 0 for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        window_counts = {char: 0 for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        
        goal = len(t_counts)
        correct_counts = 0
        min_length = None
        min_string = None
        
        left = 0
        right = 0
        
        for char in t:
            t_counts[char] += 1
        
        for char in t_counts:
            if t_counts[char] <= window_counts[char]:
                correct_counts += 1
        
        while right < len(s):
            while right < len(s) and correct_counts < goal:
                window_counts[s[right]] += 1
                
                if window_counts[s[right]] == t_counts[s[right]]:
                    correct_counts += 1
                    
                right += 1
                    
            while left < right and correct_counts == goal:
                if min_string is None:
                    min_string = (left, right)
                    min_length = right - left
                    
                elif min_length > right - left:
                    min_string = (left, right)
                    min_length = right - left
                    
                window_counts[s[left]] -= 1
                
                if window_counts[s[left]] == t_counts[s[left]] - 1:
                    correct_counts -= 1
                
                left += 1
                
        if min_string == None:
            return ""
        else:
            mleft, mright = min_string
            return s[mleft:mright]
            
            
                
        
        