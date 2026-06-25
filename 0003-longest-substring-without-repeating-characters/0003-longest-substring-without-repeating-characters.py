class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        maxLength = 0

        for right in range (len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1

            chars.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength        
        
        