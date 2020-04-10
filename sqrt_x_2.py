class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        thread = 0.0000000001
        if x < 1:
            start, end = x, 1
        else:
            start, end = 1, x
        while end - start > thread:
            mid = start + (end - start) / 2 
            if mid ** 2 < x:
                start = mid
            else: 
                end = mid

        return start
