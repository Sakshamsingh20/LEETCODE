class Solution:
    def maxBuilding(self, n, restrictions):

        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        # Left -> Right
        for i in range(1, len(restrictions)):
            dist = restrictions[i][0] - restrictions[i - 1][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # Right -> Left
        for i in range(len(restrictions) - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        ans = 0

        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            d = x2 - x1

            peak = (h1 + h2 + d) // 2

            ans = max(ans, peak)

        return ans