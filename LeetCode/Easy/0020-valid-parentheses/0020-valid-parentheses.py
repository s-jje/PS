class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for c in s:
            if c not in parentheses:
                stack.append(c)
            elif not stack or parentheses[c] != stack.pop():
                return False
        
        return len(stack) == 0