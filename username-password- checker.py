# Paswword Authentication System
# Features: user database, login check, 3 attemp lockout
# built by Dropabug
# may 2026 








user = {"richard": "test123",
        "alice": "test234",
        "bob": "test123"}

attemps = 0

while attemps < 3:
    username = input("Enter username: ")
    password = input("Enter password:")

    if username in user:
        if user[username] == password:
            print("Access granted. Welcome" + username)
            break
   
        else:
            print("Wrong password.\n")
            attemps = attemps + 1

    else:
        print("username not recognised.")        
        attemps = attemps + 1 

if attemps == 3:
    print("Account locked. Too many failed attemps.")