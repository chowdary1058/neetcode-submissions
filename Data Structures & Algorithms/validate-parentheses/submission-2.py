'''class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            elif ch in ")]}":
                if not stack:
                    return False

                if (ch == ')' and stack[-1] != '(') or \
                (ch == ']' and stack[-1] != '[') or \
                (ch == '}' and stack[-1] != '{'):
                    return False

                stack.pop()

        return len(stack) == 0
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False