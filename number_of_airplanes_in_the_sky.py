"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        event_map, cur_result, result = [], 0, 0
        for airplane in airplanes:
            event_map.append([airplane.start, 1])
            event_map.append([airplane.end, -1])

        for _, event in sorted(event_map):
            cur_result += event
            result = max(cur_result, result)
        return result


