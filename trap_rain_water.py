import heapq


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
        result, boards_heap, visited = 0, [], set([])
        self.find_boards(boards_heap, visited, heights)

        while boards_heap:
            height, cur_x, cur_y = heapq.heappop(boards_heap)
            for next_x, next_y in self.get_next_cell(cur_x, cur_y, visited, heights):
                result += max(0, height - heights[next_x][next_y])
                heapq.heappush(boards_heap, (max(height, heights[next_x][next_y]), next_x, next_y))
                visited.add((next_x, next_y))
        return result

    def find_boards(self, input_heap, visited, heights):
        x_length, y_length = len(heights), len(heights[0])
        for x_index in range(x_length):
            heapq.heappush(input_heap, (heights[x_index][0], x_index, 0))
            heapq.heappush(input_heap, (heights[x_index][y_length - 1], x_index, y_length - 1))
            visited.add((x_index, 0))
            visited.add((x_index, y_length - 1))
        for y_index in range(y_length):
            heapq.heappush(input_heap, (heights[0][y_index], 0, y_index))
            heapq.heappush(input_heap, (heights[x_length - 1][y_index], x_length - 1, y_index))
            visited.add((0, y_index))
            visited.add((x_length - 1, y_index))

    def get_next_cell(self, x, y, visited, matrix):
        result, x_length, y_length = [], len(matrix), len(matrix[0])
        for dx, dy in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
            next_x = dx + x
            next_y = dy + y
            if 0 <= next_x < x_length and 0 <= next_y < y_length and (next_x, next_y) not in visited:
                result.append((next_x, next_y))
        return result

