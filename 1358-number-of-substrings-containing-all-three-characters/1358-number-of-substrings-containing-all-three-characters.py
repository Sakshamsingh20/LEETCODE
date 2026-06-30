class Solution(object):
    def numberOfSubstrings(self, s):
       
        # Track the most recent index where we saw 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            last_seen[char] = i
            
            # The number of valid substrings ending at index i is bounded 
            # by the smallest index of the three characters we've seen so far.
            # We add 1 because string indices are 0-based.
            # If a character hasn't been seen, the min will be -1, adding 0 to count.
            count += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
            
        return count
        