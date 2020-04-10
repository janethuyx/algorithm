class Solution:
    """
    @param S: string S
    @param T: string T
    @return: Backspace String Compare
    """

    def backspaceCompare(self, S, T):
        # Write your code here
        if not S and not T:
            return True
        if not S or not T:
            return False
        return self.get_final_string(S) == self.get_final_string(T)

    def get_final_string(self, input_string):
        stack = []
        for char in input_string:
            if char != "#":
                stack.append(char)
                continue
            if stack:
                stack.pop()
        return "".join(stack)
