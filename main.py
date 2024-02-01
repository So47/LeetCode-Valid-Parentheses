class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'}

        stack = []
        for char in s:
            if char in brackets: # if it's open bracket we append it to the stack
                stack.append(char)
            elif not stack or brackets[stack.pop()] != char: # For close bracket we check if the stack not empty then we check if it's the correct bracket
                return False    
                    
        return len(stack) == 0    # if we didn't pop a close bracket for an open bracket that means it's invalid and vice versa      


   
