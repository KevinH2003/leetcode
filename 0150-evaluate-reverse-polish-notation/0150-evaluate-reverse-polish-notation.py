class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        expressions = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y if (x / y) >= 0 else math.ceil(x / y)
        }
        
        for token in tokens:
            if token in expressions:
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    
                    stack.append(expressions[token](a, b))
            else:
                stack.append(int(token))
                    
        return stack.pop()