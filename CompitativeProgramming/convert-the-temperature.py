class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        celsius=round(celsius,2)
    
        return [celsius+273.15 , celsius*1.80 + 32.00]

        