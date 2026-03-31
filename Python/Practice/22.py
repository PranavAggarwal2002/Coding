def is_leap_year(year): 
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) 
year = 2024 
print(is_leap_year(year)) 