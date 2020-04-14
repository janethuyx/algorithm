

class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        if not nums or len(nums) == 1:
            return 0
        count_map, result,cur_count = {}, 0, 0
        for num_index in range(len(nums)):
            if num_index == 0:
                count_map[cur_count] = [0]
            if nums[num_index] == 1:
                cur_count -= 1
            else:
                cur_count += 1
            if cur_count not in count_map:
                count_map[cur_count] = [num_index+1]
            else:
                count_map[cur_count].append(num_index+1)
                result = max(result, count_map[cur_count][-1] - count_map[cur_count][0])
        return result


