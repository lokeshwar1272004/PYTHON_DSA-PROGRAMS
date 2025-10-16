class Solution:
    def minimumRecolors(self,blocks,k):
        blocks=list(blocks)
        count=0
        change=0
        mini=float('inf')
        for i in range(len(blocks)):
            for j in range(i,len(blocks)):
                if blocks[j]!='B':
                    change+=1
                count+=1
                if count==k:
                    mini=min(mini,change)
                    change=0
                    break
            count=0
        return mini
a=Solution()
b='BWWWBB'
k=6
print(a.minimumRecolors(b,k))