def isValid(self, s: str) -> bool:
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            openBracket = stack.pop(-1)
            if (openBracket=='(' and c != ')') or (openBracket=='[' and c != ']')  or (openBracket=='{' and c != '}'):
                return False
    if len(stack) != 0:
        return False
    return True

# Time Complexity - O(n)
# Space Complexity - O(n)