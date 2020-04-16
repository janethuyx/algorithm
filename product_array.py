

class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        left_product, right_product, result, length = 1, 1, [], len(nums)
        result = [1 for _ in range(length)]
        for index in range(length):
            result[index] *= left_product
            result[length - index - 1] *= right_product
            left_product *= nums[index]
            right_product *= nums[length - index - 1]
        return result


