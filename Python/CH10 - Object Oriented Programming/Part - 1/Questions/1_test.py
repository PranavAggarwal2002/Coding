class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


l = Programmer("lakhan", 120000, 245001)
print(l.name, l.salary, l.pincode, l.company)
r = Programmer("Rohan", 120000, 245001)
print(r.name, r.salary, r.pincode, r.company)