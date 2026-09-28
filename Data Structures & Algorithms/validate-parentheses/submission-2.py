class Solution:
    def isValid(self, s: str) -> bool:
        stack, valid = [], {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in valid:
                if not stack:
                    return False
                open_c = stack.pop()
                if valid[c] != open_c:
                    return False
            else:
                stack.append(c)
        return True if not stack else False