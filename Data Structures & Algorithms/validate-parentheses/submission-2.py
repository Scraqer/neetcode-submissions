class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching:
                if not Stack or Stack[-1] != matching[char]:
                    return False
                Stack.pop()
            else:
                Stack.append(char)
        return len(Stack) == 0


                
                






