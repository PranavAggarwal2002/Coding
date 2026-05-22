class Employee: #Class
    language = "Python" # Class Attribute
    salary = 120000 # Class Attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # Is  a way to define construcotr which don't need self 
    def greet():
        print("Good Morning")


ram = Employee()
ram.language = "JavaScript" # Object Attribute/ Instance Attribute

ram.greet()
ram.getInfo()

