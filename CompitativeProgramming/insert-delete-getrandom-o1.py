class RandomizedSet:

    def __init__(self):
        self.rondem=set()
        
        

    def insert(self, val: int) -> bool:
        if val in self.rondem:
            return False
        self.rondem.add(val)
        return True
        

        

    def remove(self, val: int) -> bool:
        if val in self.rondem:
            self.rondem.remove(val)

            return True
        return False
        

    def getRandom(self) -> int:
        arry=list(self.rondem)
        return random.choice(arry)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()