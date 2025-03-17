class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif stack:
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                else:  
                    return False 
            else:
                return False  

        return not stack  
