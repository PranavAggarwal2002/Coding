marks = {
    "Pranav": 100,
    "Pratham":75,
    "Rahul": 34,
    0:"Totum"
}
print(marks.items())
print(marks.keys()) # right side of dics contain keys
print(marks.values()) # Left side of dics contain values
marks.update({"Pranav":99,"Divs":100}) #This update old value as well add new values if not present
print(marks)

print(marks.get("Pranav"))
print(marks.get("Remu"))
print(marks["Remu"])
# Why use print(marks.get("Pranav")) when print(marks["Pranav"]) will do same?
# .get will give youe None where as other will give you an error which is bad