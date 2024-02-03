class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        j=0
        nBlack=0
        subString= blocks[0:k]
        for i in subString:
            if i == "B":
                nBlack+=1
        count=max(count,nBlack)

        for i in range(k,len(blocks)):
            if blocks[i]=="B":
                nBlack+=1
            if blocks[j]== "B":
                nBlack-=1
            j+=1
            count=max(count,nBlack)
        return k-count
        