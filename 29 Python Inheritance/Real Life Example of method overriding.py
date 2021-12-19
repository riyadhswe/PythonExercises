class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8

b1 = Bank()
b2 = SBI()
b3 = ICICI()

print(b1.getroi())
print(b2.getroi())
print(b3.getroi())
