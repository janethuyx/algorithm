import heapq


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """

    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        if len(nums) == 1:
            return nums[:]
        self.max_heap, self.min_heap = [], []
        result = []
        for index in range(len(nums)):
            if len(self.max_heap) == 0 or nums[index] <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -nums[index])
            else:
                heapq.heappush(self.min_heap, nums[index])
            self.balance()

            if index >= k:
                if nums[index - k] <= -self.max_heap[0]:
                    self.max_heap.remove(-nums[index - k])
                    heapq.heapify(self.max_heap)
                else:
                    self.min_heap.remove(nums[index - k])
                    heapq.heapify(self.min_heap)
                self.balance()

            if index >= k - 1:
                result.append(-self.max_heap[0])

        return result

    def balance(self):
        while len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        while len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
  
