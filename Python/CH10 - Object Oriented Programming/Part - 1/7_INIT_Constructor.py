class Employee:
    language = "Python" 
    salary = 120000 

    def __init__(self, name, salary, language): # Dunder method which is automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


ram = Employee("Ram", 130000, "Javascript")

print(ram.name, ram.salary, ram.language)