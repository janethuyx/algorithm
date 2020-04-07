class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ""
        stack = []
        for letter in s:
            if letter != "]":
                stack.append(letter)
                continue

            sub_str_stack = []
            while stack and stack[-1] != "[":
                sub_str_stack.append(stack.pop())

            stack.pop()

            number, base = 0, 1
            while stack and stack[-1] in "0123456789" and stack[-1]:
                number += ((ord(stack.pop()) - ord('0')) * base)
                base *= 10

            sub_str = "".join(reversed(sub_str_stack)) * number
            stack.append(sub_str)

        return "".join(stack)

