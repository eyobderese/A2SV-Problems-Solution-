class Bitset:

    def __init__(self, size: int):
        self.bits=set()
        self.bitsz={i for i in range(size)}
        self.size=size
        

    def fix(self, idx: int) -> None:
        self.bits.add(idx)
        self.bitsz.discard(idx)
        

        

    def unfix(self, idx: int) -> None:
        
        self.bits.discard(idx)
        self.bitsz.add(idx)
                

        

    def flip(self) -> None:
        self.bits,self.bitsz=self.bitsz,self.bits
            

                
        

    def all(self) -> bool:
        if len(self.bits)==self.size:
            return True
        return False
        

    def one(self) -> bool:
        if self.bits:
            return True
        return False

        

    def count(self) -> int:
        return len(self.bits)
        
        

    def toString(self) -> str:
        res=''
        for i in range(self.size):
            if i in self.bits:

                res+="1"
            else:
                res+="0"
        return res

       
      
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()