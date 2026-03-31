Mark1 = float(input("Enter Marks of Subject 1 : "))
Mark2 = float(input("Enter Marks of Subject 2 : "))
Mark3 = float(input("Enter Marks of Subject 3 : "))

#check for total percentage
total_percentage = (Mark1 + Mark2 + Mark3)/3
# total_percentage = (100*(Mark1 + Mark2 + Mark3))/300

if(total_percentage>=40 and Mark3>33 and Mark2>33 and Mark1>33):
    print("You Have Passed",total_percentage)
else:
    print("You have failed, try again next year:",total_percentage)
