class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        # Offset to handle negative prefix sums in our 1-indexed Fenwick tree
        offset = n + 2
        bit = [0] * (2 * n + 5)
        
        def update(index, val):
            while index < len(bit):
                bit[index] += val
                index += index & (-index)
                
        def query(index):
            res = 0
            while index > 0:
                res += bit[index]
                index -= index & (-index)
            return res
        
        # Initial state
        update(0 + offset, 1)
        
        ans = 0
        curr_sum = 0
        
        for num in nums:
            if num == target:
                curr_sum += 1
            else:
                curr_sum -= 1
            
            # Count valid previous prefix sums
            ans += query(curr_sum - 1 + offset)
            
            # Add current prefix sum to the tree
            update(curr_sum + offset, 1)
            
        return ans