import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while heap:
            max_value = -heapq.heappop(heap)
            if not heap:
                return max_value
            else:
                diff = max_value + heapq.heappop(heap)
                heapq.heappush(heap, -diff)
        return 0

