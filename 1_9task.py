class calculater:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def exponent(self,a,b):
        print(a**b)
    def floordiv(self,a,b):
        print(a//b)
    def mod(self,a,b):
        print(a%b)

    def describe(self):
        print(self.model,self.madein,self.color,self.discount)



obj1=calculater()
obj2=calculater()
obj3=calculater()

obj1.add(2,3)
obj1.sub(2,3)
obj1.mul(2,3)
obj1.exponent(2,3)
obj1.floordiv(2,3)
obj1.mod(2,3)


obj2.add(5,9)
obj2.sub(5,9)
obj2.mul(5,9)
obj2.exponent(5,9)
obj2.floordiv(5,9)
obj2.mod(5,9)


obj3.add(3,7)
obj3.sub(3,7)
obj3.mul(3,7)
obj3.exponent(3,7)
obj3.floordiv(3,7)
obj3.mod(3,7)


obj1.model = "M123"
obj1.madein = "India"
obj1.color = "Red"
obj1.discount = "10%"

obj2.model = "M123"
obj2.madein = "India"
obj2.color = "Red"
obj2.discount = "10%"

obj1.describe()
obj2.describe()