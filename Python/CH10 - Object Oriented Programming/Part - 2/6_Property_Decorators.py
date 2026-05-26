# Property decorator
class Employee: # Here encapsulation happen as we have packed many working compnent in class
    a=1
    @classmethod
    def show(cls):
        print(f"The Class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.firstname} {self.lastname}"
    
    @name.setter #Here abssraction happen as user doesn't know how much work we are doing that we separating name here 
    def name (self, value): #Implementation detail hidden from user
        self.firstname = value.split(" ")[0]
        self.lastname = value.split(" ")[1]

e = Employee()
e.a = 45
e.name = "Rohan Raj"
print(e.firstname, e.lastname)
e.show()