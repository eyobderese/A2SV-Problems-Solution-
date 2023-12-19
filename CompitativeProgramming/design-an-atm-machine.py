class ATM:

    def __init__(self):
        self.atm= defaultdict(int)
        self.nots=[20,50,100,200,500]
        self.temp={}
        

    def deposit(self, banknotesCount: List[int]) -> None:
        
        k=0
        for i in self.nots:
            self.atm[i]+=banknotesCount[k]
            k+=1
        
       

    def withdraw(self, amount: int) -> List[int]:
        self.temp=copy.deepcopy(self.atm)
        print(self.atm)
        
        tracker=defaultdict(int)
        while amount>0:
            if amount>=500 and self.atm[500]>0:
                n_500= min(self.atm[500],amount//500)
                amount-=(500)*n_500
                self.atm[500]-=n_500
                tracker[500]+=n_500
            elif amount>=200 and self.atm[200]>0:
                n_200= min(self.atm[200],amount//200)
                amount-=(200)*n_200
                self.atm[200]-=n_200
                tracker[200]+=n_200
            elif amount>=100 and self.atm[100]>0:
                n_100= min(self.atm[100],amount//100)
                amount-=(100)*n_100
                self.atm[100]-=n_100
                tracker[100]+=n_100
            elif amount>=50 and self.atm[50]>0:
                n_50= min(self.atm[50],amount//50)
                amount-=(50)*n_50
                self.atm[50]-=n_50
                tracker[50]+=n_50
            elif amount>=20 and self.atm[20]>0:
                n_20= min(self.atm[20],amount//20)
                amount-=(20)*n_20
                self.atm[20]-=n_20
                tracker[20]+=n_20
            else:
                self.atm=copy.deepcopy(self.temp)
                return [-1]
              
        ans=[]
        for i in self.nots:
            ans.append(tracker[i])
               
        return ans
        

            
        

        
       