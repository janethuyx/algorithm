

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        x_length, y_length = len(matrix), len(matrix[0])
        dp = [[0 for y in range(y_length)] for x in range(x_length)]
        for y in range(y_length):
            dp[0][y] = matrix[0][y]

        result = max(dp[0])
        for x in range(1 ,x_length):
            dp[x][0] = matrix[x][0]
            for y in range(1, y_length):
                if matrix[x][y]:
                    dp[x][y] = min(dp[ x -1][ y -1], dp[x][ y -1], dp[ x -1][y]) + 1
                else:
                    dp[x][y] = 0
            result = max(result, max(dp[x]))
        return result ** 2




