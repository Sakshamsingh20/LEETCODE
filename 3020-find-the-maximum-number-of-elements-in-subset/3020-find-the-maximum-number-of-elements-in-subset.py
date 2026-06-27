

class Solution:
    def maximumLength(self, nums):
        counts = Counter(nums)
        max_len = 1
        
        # Special case for the number 1
        if 1 in counts:
            ones = counts[1]
            # If the count of 1s is even, we use (ones - 1) to make it an odd-length peak sequence
            max_len = ones if ones % 2 == 1 else ones - 1
            
        # Check sequences starting from every unique number
        for x in counts:
            if x == 1:
                continue
            
            curr = x
            curr_len = 0
            
            # As long as we have pairs, we can continue building the sides of the mountain
            while counts[curr] >= 2:
                curr_len += 2
                curr *= curr  # Square the current number
                
            # If we found a single instance of the next square, it caps the mountain perfectly
            if counts[curr] == 1:
                curr_len += 1
            # If it's 0, the last processed number (which had >= 2 copies) has to be our peak
            else:
                curr_len -= 1 
                
            max_len = max(max_len, curr_len)
            
        return max_len