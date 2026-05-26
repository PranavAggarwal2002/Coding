# Super Method is way is way for a child to run it's parent contrcutor as well with itself
class Employee:
    def __init__(self):
        print("Contructor of Employee")
    
class Coder(Employee):
    def __init__(self):
        print("Contructor of Coder")

class Programmer(Coder):
    def __init__(self):
        super().__init__() # It make it run it's parent constructor as well but not granparent constructor
        print("Contructor of Programmer")

o = Employee()

o = Coder()

o = Programmer()
