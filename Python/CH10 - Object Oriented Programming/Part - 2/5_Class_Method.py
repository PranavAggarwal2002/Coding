# Class Method is way is way for a programmer to access class directly in a method
class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The Class value of a is {cls.a}")

e = Employee()
e.a = 45

e.show() # Now here it show 1 instead of 45 as class atrribute is now like fixed