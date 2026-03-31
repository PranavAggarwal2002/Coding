name = "pranav"

print("string is",name)
print("len() give lenght of string",len(name))

print("To check if string ends with nav",name.endswith("nav"))
print("To check if string start with pr",name.startswith("pr"))
print("To Capitalize the first charcter of string",name.capitalize())
print("if string has a space in 0", "' pranav'")
p = " pranav"
print("the captilize will work on space only",p.capitalize())

print("if string is", "hello world 123")
p = "hello world 123"
index = p.find("or")
print("then the function index() find the world and give it's index here for 'or'",index)
rep = p.replace("world", "Python")
print("then replace() replaces a word in sting the with new word here Python with world", rep)