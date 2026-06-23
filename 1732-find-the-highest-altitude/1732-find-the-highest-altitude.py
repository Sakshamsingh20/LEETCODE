class Solution(object):
    def largestAltitude(self, gain):

        current = 0
        highest = 0

        for g in gain:

            current = current + g
            highest = max(highest,current)

        return highest    
        
