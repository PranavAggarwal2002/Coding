class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n

    def __truediv__(self, num):
        return self.n / num.n
    
    def __floordiv__(self, num):
        return self.n // num.n
    
    def str__():
        pass

    def __len__(self):
        pass

n = Number(1)
m = Number(2)

print(n+m)
print(n//m)