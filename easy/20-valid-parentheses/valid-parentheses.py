class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paremDict = {')':'(', '}':'{', ']':'['}
        if len(s) == 1:
            return False
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in paremDict.keys():
                if not stack or paremDict[c] != stack.pop():
                    return False
        return not stack