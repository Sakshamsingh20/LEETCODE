class Solution:
    def maxIceCream(self, costs, coins):

        max_cost = max(costs)

        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        count = 0

        for price in range(1, max_cost + 1):

            while freq[price] > 0 and coins >= price:

                coins -= price
                count += 1
                freq[price] -= 1

        return count