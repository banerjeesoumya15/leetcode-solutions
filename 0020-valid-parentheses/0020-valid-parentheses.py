class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n == 1:
            return False
        if n%2 != 0:
            return False
        braces = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        if (s[0] in braces.values()) or (s[-1] in braces.keys()):
            return False
        for char in s:
            if not stack and char in braces.values():
                return False
            if char in braces.keys():
                stack.append(char)
            else:
                c = stack.pop()
                if braces[c] != char:
                    # print(c, braces[c])
                    return False
        if stack:
            return False
        return True
        