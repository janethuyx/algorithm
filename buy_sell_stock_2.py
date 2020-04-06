class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        result, stack, length = 0, [], len(prices)
        for index in range(length + 1):
            price = prices[index] if index < length else -1
            if stack and prices[stack[-1]] > price:
                buy_price, sell_price = prices[stack[0]], prices[stack[-1]]
                result += (sell_price - buy_price)
                stack = []

            stack.append(index)
        return result
