class Solution:
    def isValid(self, s: str) -> bool:
        hashh = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i not in hashh:
                stack.append(i)
            else:
                if (not stack) or (stack.pop() != hashh[i]):
                    return False

        return len(stack) == 0
