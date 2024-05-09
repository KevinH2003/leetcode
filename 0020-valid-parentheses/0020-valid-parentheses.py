class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {'(': ')', '{': '}', '[': ']'}
        
        for c in s:
            if c in parens.keys():
                stack.append(parens[c])
            else:
                if len(stack) < 1:
                    return False
                if stack.pop() != c:
                    return False
        
        return True if len(stack) == 0 else False
                