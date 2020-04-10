
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            pieces = self.get_pieces(L, mid)
            if pieces < k:
                end = mid
            else:
                start = mid
        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
        return 0

    def get_pieces(self, L, input_length):
        pieces = 0
        for length in L:
            pieces += length // input_length
        return pieces


