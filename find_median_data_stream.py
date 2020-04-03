import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return []
        if len(nums) == 1:
            return nums[:]
        result, max_heap, min_heap, median = [nums[0]], [-nums[0]], [], nums[0]
        for index in range(1,len(nums)):
            cur = nums[index]
            if cur <= median:
                heapq.heappush(max_heap, -cur)
            else:
                heapq.heappush(min_heap, cur)
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            median = -max_heap[0]
            result.append(median)
        return result

