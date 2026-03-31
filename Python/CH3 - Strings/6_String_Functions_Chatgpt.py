s = "  hello world  "
s2 = "banana"
num = "12345"
mix = "Hello123"

print("Original string:", s)

# Case functions
print("lower() -> converts all characters to lowercase:", s.lower())
print("upper() -> converts all characters to uppercase:", s.upper())
print("title() -> capitalizes first letter of every word:", s.title())
print("capitalize() -> capitalizes first letter of string:", s.capitalize())
print("swapcase() -> swaps lowercase to uppercase and vice versa:", s.swapcase())

# Strip functions
print("strip() -> removes spaces from both sides:", s.strip())
print("lstrip() -> removes spaces from left side:", s.lstrip())
print("rstrip() -> removes spaces from right side:", s.rstrip())

# Search functions
print("find('world') -> returns index of substring:", s.find("world"))
print("count('a') -> counts occurrences of 'a' in string:", s2.count("a"))
print("startswith('  he') -> checks if string starts with given value:", s.startswith("  he"))
print("endswith('  ') -> checks if string ends with given value:", s.endswith("  "))

# Replace
print("replace('world','python') -> replaces substring:", s.replace("world", "python"))

# Split and join
words = s.strip().split(" ")
print("split() -> splits string into list:", words)

joined = "-".join(words)
print("join() -> joins list elements into string with separator:", joined)

# Checking functions
print("isalpha() -> checks if string contains only letters:", "hello".isalpha())
print("isdigit() -> checks if string contains only digits:", num.isdigit())
print("isalnum() -> checks if string contains letters and numbers:", mix.isalnum())
print("isspace() -> checks if string contains only spaces:", "   ".isspace())
print("islower() -> checks if all letters are lowercase:", "hello".islower())
print("isupper() -> checks if all letters are uppercase:", "HELLO".isupper())

# Formatting
name = "Pranav"
age = 20
print("f-string -> modern string formatting:", f"My name is {name} and I am {age}")