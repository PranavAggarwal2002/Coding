class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): # Here + means multiplication.(It will work properly as well)
        return self.n * num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n

    def __truediv__(self, num): # Here / means string Hello .(It will work properly as well)
        return "Hello"
    
    def __floordiv__(self, num): # Here // means multiplication.(It will work properly as well)
        return self.n - num.n

n = Number(1)
m = Number(2)

print(n/m)
print(n+m) 
print(n//m)

'''
| Operator | Dunder Method  |
| -------- | -------------- |
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `//`     | `__floordiv__` |

Python does not care what logic you put inside them.

Python only says:

“Call __add__ and return whatever it returns"
'''