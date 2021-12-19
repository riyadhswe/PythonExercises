class Calculation1:
    def Summation(self, a, b):
        return a + b


class Calculation2:
    def Multiplication(self, a, b):
        return a * b

class Calculation3:
    def Subtraction(self,a,b):
        return a - b


class Derived(Calculation1, Calculation2,Calculation3):
    def Divide(self, a, b):
        return a / b


d = Derived()
print(d.Summation(10, 20))
print(d.Subtraction(10, 20))
print(d.Multiplication(10, 20))
print(d.Divide(10, 20))
