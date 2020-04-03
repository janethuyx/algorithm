class Solution:
    def isHappy(self, input_number: int) -> bool:
        visited = set()
        while input_number > 1 and input_number not in visited:
            visited.add(input_number)
            input_number = self.get_next_number(input_number)
        return input_number == 1

    def get_next_number(self, input_number):
        base, total = 10, 0
        while input_number > 0:
            total += (input_number % base) ** 2
            input_number = input_number // base
        return total


