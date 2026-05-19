import hashlib

passwords = {
    "richard": "test123",
    "alice": "test234",
    "bob": "test123"
}

for user, pwd in passwords.items():
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    print(user, "-->", hashed)