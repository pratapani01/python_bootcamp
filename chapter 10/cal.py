class Calculator:
    def __init__(self, n):
        self.n = n
    def sqr(self):
        print(f"the sqaure is {self.n*self.n}")
    def cub(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def sqt(self):
        print(f"the sqaure root is {self.n**1/2}")
a= Calculator(4)

a.sqr()
a.cub()
a.sqt()