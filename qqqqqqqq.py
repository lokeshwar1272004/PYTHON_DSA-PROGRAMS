class Solution:
    def findMissing(self, a, b, n, m):
        self.a = list(a)
        self.b = list(b)
        self.n = n
        self.m = m
        for i in range(n):
            if self.a[i] not in self.b:
                print(self.a[i])
a = {1,2,3,4}
b = {1,2,5}
n = 4
m = 4
c = Solution()
c.findMissing(a,b,n,m)


elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
print("..",len(elements))
