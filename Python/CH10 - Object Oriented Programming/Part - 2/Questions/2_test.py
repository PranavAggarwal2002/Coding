class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bark")

d = Dog()
d.bark()