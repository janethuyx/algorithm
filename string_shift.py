
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        result,length, shift_steps = ['' for i in range(len(s))], len(s), 0
        for direction in shift:
            if direction[0] == 1:
                shift_steps += direction[1]
            else:
                shift_steps -= direction[1]
        for char_index in range(length):
            result[(char_index + shift_steps) % length] = s[char_index]
        return ''.join(result)


