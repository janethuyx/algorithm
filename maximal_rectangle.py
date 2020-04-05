class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """

    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix:
            return 0

        result = 0
        for row_index in range(len(matrix)):
            for column_index in range(len(matrix[0])):
                cur = matrix[row_index][column_index]
                if cur:
                    matrix[row_index][column_index] = 1
                else:
                    matrix[row_index][column_index] = 0
                if row_index == 0:
                    prev = 0
                else:
                    prev = matrix[row_index - 1][column_index]
                if cur == 0:
                    continue
                matrix[row_index][column_index] = cur + prev
            cur_height = matrix[row_index]
            result = max(result, self.largest_rectangle_area(cur_height))
        return result

    def largest_rectangle_area(self, height):
        result, stack, length = 0, [], len(height)
        for index in range(length + 1):
            h = height[index] if index < length else -1
            while stack and height[stack[-1]] >= h:
                cur_h = height[stack.pop()]
                left_index = stack[-1] if stack else -1
                cur_length = index - left_index - 1
                result = max(result, cur_h * cur_length)
            stack.append(index)
        return result

