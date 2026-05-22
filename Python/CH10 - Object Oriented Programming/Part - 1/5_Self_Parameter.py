class Employee: #Class
    language = "Python" # Class Attribute
    salary = 120000 # Class Attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


ram = Employee()
ram.language = "JavaScript" # Object Attribute/ Instance Attribute

Employee.getInfo(ram)
#          or 
ram.getInfo() # both are same as ram.getInfo() change to Employee.getInfo(ram) only
