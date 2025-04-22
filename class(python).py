'''a = 3+6j
b = 4 - 3j
print(a, type(a))
print(b, type(b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)'''

class xcomplex:
    def __add__ (self, other):
        ans = xcomplex()
        ans.r = self.r + other.r
        ans.i = self.i + other.i
        return ans
    def __init__(self,r=0,i=0):
        self.r = r
        self.i = i
    def __str__(self):
        return f'({self.r} {self.i:+}i)'
a = xcomplex(3,6)
b = xcomplex(4, -3)
c = xcomplex()
print(a)
print(b)
print(a+b)


