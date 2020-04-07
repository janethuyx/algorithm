class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """

    def groupAnagrams(self, strs):
        # write your code here
        result_map = {}
        for string in strs:
            key = self.get_letter_number(string)
            if key in result_map:
                result_map[key].append(string)
            else:
                result_map[key] = [string]

        return result_map.values()

    def get_letter_number(self, input_string):
        result = [0] * 26
        for char in input_string:
            result[ord(char) - ord('a')] += 1
        return ''.join([str(char) for char in result])

