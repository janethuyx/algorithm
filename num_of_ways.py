
class Solution:
    def numOfWays(self, n):
        dp = [[[[0 for x1 in range(3)] for x2 in range(3)] for x3 in range(3)] for y in range(n)]
        result, mod = 0, 10 ** 9 + 7
        for x1 in range(3):
            for x2 in range(3):
                for x3 in range(3):
                    if x1 != x2 and x2 != x3:
                        dp[0][x1][x2][x3] += 1
        for y in range(1, n):
            for x1 in range(3):
                for x2 in range(3):
                    for x3 in range(3):
                        for pre_x1 in range(3):
                            for pre_x2 in range(3):
                                for pre_x3 in range(3):
                                    if x1 != x2 and x2 != x3 and pre_x1 != x1 \
                                            and pre_x2 != x2 and pre_x3 != x3:
                                        if dp[y - 1][pre_x1][pre_x2][pre_x3] > 0:
                                            dp[y][x1][x2][x3] += dp[y - 1][pre_x1][pre_x2][pre_x3]
                                            dp[y][x1][x2][x3] %= mod

        for x1 in range(3):
            for x2 in range(3):
                for x3 in range(3):
                    result += dp[n - 1][x1][x2][x3]
                    result %= mod
        return result

