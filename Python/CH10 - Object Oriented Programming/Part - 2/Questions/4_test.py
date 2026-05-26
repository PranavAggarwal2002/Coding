class Employee:
    salary = 234
    increment = 20

    @property
    def SalryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @SalryAfterIncrement.setter
    def SalryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100


e = Employee()
# print(e.SalryAfterIncrement)

e.SalryAfterIncrement = 280.8
print(e.increment)