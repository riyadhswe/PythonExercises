class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print("Name : ",self.name,"ID : ",self.id)


S1 = Student("A",101)
S2 = Student("B",102)

S1.display()
S2.display()