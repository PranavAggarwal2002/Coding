P1 = "Make a lot of money"
P2 = "buy now"
P3 = "Subscribe this"
P4 = "Click this"

message = input("Enter your comment: ")

# Cleaner would be : if((P1 in message) or (P2 in message) or (P3 in message) or (P4 in message)):
if(P1 in message or P2 in message or P3 in message or P4 in message):
    print("This comment is a spam")
else:
    print("This is not a spam")