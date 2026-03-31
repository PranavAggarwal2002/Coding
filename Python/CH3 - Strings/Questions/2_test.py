letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
letter1 = "'Dear <|Name|>, " \
"You are selected! " \
"<|Date|>'"
letter2 = "'Dear <|Name|>, " \
"\nYou are selected! " \
"\n<|Date|>'"
print(letter.replace("<|Name|>", "Pranav").replace("<|Date|>", "21 March 2026"))
print(letter1.replace("<|Name|>", "Pranav").replace("<|Date|>", "21 March 2026"))
print(letter2.replace("<|Name|>", "Pranav").replace("<|Date|>", "21 March 2026"))