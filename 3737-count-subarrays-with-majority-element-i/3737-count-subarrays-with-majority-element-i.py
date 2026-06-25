class Solution:
    def countMajoritySubarrays(self, nums, target):

        arr = []

        for num in nums:
            if num == target:
                arr.append(1)
            else:
                arr.append(-1)

        ans = 0

        for i in range(len(arr)):

            s = 0

            for j in range(i, len(arr)):

                s += arr[j]

                if s > 0:
                    ans += 1

        return ans