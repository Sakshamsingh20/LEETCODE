class Solution(object):
    def angleClock(self, hour, minutes):
       hour %= 12
       hour_angle= hour*30 + minutes*0.5
       minutes_angle = minutes*6
       diff= abs(hour_angle - minutes_angle)

       return min(diff,360-diff)
       
        