import json
user = {
    "richard": "hashgoeshere" ,
    "alice": "hashgoeshere2",
}
with open("test_users.json", "w") as f:
    json.dump(user, f)  

print ("saved")

with open ("test_users.json", "r") as f:
    loaded = json.load(f)

print (loaded)  