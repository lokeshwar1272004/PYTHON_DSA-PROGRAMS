class Solution:
    def checkPowersOfThree(self,n):
        i=0
        while 3**i<=n:
            i+=1
        i-=1
        while i>=0:
            power=3**i
            if power<=n:
                n-=power
            i-=1
        return n==0
a=Solution()
print(a.checkPowersOfThree(21))