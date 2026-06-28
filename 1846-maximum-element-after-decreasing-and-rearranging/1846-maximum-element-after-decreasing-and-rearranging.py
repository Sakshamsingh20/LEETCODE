class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: The first element must be 1
        arr[0] = 1
        
        # Step 3: Iterate through the rest of the array
        for i in range(1, len(arr)):
            # The current element can be at most 1 greater than the previous
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # The last element will be the maximum possible value
        return arr[-1]