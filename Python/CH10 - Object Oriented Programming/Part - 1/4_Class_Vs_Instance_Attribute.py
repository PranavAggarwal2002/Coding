class Employee: #Class
    language = "Python" # Class Attribute
    salary = 120000 # Class Attribute

# Here we have created a class where every employee language Python and salary 120000

ram = Employee()
ram.language = "JavaScript" # Object Attribute/ Instance Attribute
print(ram.language, ram.salary)

# Here Employee language will be printed as JavaScript
# As Instance Attribute takeover Class Attribute