import json
import hashlib

users = {
    "richard": hashlib.sha256("test123" .encode()).hexdigest(),
    "alice": hashlib.sha256("test234" .encode()).hexdigest(),
    "bob": hashlib.sha256("test123" .encode()).hexdigest()      
}

with open("users.json", "w") as f:  
    json.dump(users, f) 

    print("users.json created")
    print(users)