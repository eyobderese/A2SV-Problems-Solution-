class FrequencyTracker(object):

    def __init__(self):
        self.tracker=defaultdict(int)
        self.frq=defaultdict(list)
        

        

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.tracker[number]==0:
            self.tracker[number]+=1
            self.frq[self.tracker[number]].append(number)
        else:
            self.tracker[number]+=1
            self.frq[self.tracker[number]].append(number)
            self.frq[self.tracker[number]-1].remove(number)

            



        
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.tracker[number]==0:
            pass
            
        else:
            self.tracker[number]-=1
            self.frq[self.tracker[number]].append(number)
            self.frq[self.tracker[number]+1].remove(number) 
        


        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if self.frq[frequency]:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)