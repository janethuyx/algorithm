
class Solution:
    def countElements(self, arr: List[int]) -> int:
        result, element_map = 0, {}
        for num in arr:
            if num not in element_map:
                element_map[num] = 1
        for num in arr:
            if num + 1 in element_map:
                result += 1

        return result

