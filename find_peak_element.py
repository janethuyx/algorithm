
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) //2
            if A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        if A[start] < A[end]:
            return end
        return start

