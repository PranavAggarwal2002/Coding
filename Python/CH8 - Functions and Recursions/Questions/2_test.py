def ctof():
    c = float(input("Enter Temp in Celsius : "))
    f = (((c/5)*9)+32)
    return(f" temp in fahrenheit is {f}")
    #print(f"Temp in fahrenheit is {f}")

print(ctof())
#ctof()

#Harry Bhai way
def c_to_f(c):
    return(((c/5)*9)+32)
c = float(input("Enter Temp in Celsius : "))
c = round(c_to_f(c), 2)
print(f"{c} fahrenhite")
