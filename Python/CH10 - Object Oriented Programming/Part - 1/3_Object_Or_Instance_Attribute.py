class Employee: #Class
    language = "Py" # Class Attribute
    salary = 120000 # Class Attribute

# Here we have created a class where every employee  language Py and salary 120000

ram = Employee()
ram.name = "Ram Robinson" # Object Attribute/ Instance Attribute
print(ram.name, ram.language, ram.salary)

rohan = Employee()
rohan.name = "Rohan Sharma" # Object Attribute/ Instance Attribute
print(rohan.name, rohan.salary, rohan.language)

# Here Language and salary are attribute of class rather than object
# Whereas ram.name = "Ram Robinson" and rohan.name = "Rohan Sharma" are Instance Attribute mean Object Attribute