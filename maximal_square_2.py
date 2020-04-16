
class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def maxSquare2(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        x_length, y_length = len(matrix), len(matrix[0])
        dp = [[0 for y in range(y_length)] for x in range(x_length)]
        up = [[0 for y in range(y_length)] for x in range(x_length)]

        for y in range(y_length):
            dp[0][y] = matrix[0][y]
            up[0][y] = 1 - matrix[0][y]

        result = max(dp[0])
        for x in range(1, x_length):
            left = 1 - matrix[x][0]
            dp[x][0] = matrix[x][0]
            up[x][0] = 0 if matrix[x][0] else matrix[ x -1][0] + 1
            for y in range(1, y_length):
                if matrix[x][y]:
                    dp[x][y] = min(dp[ x -1][ y -1], left, up[ x -1][y]) + 1
                    left = 0
                    up[x][y] = 0
                else:
                    left += 1
                    up[x][y] = up[ x -1][y] + 1
                    dp[x][y] = 0
            result = max(max(dp[x]), result)
        return result ** 2

