
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
        if self.get_least_people(pages, start) > k:
            return end
        return start

    def get_least_people(self, pages, time_limit):
        total_people, cur_time = 0, 0
        for page in pages:
            if page + cur_time > time_limit:
                total_people += 1
                cur_time = 0
            cur_time += page

        return total_people + 1

