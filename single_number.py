

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1
        for num in num_map:
            if num_map[num] == 1:
                return num


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        return 2 * sum(set(nums)) - sum(nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = 0
        for num in nums:
            a ^= num
        return a


