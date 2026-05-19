# IAM Authentication system
# login system with 3 attemps lockout
# audit log with timestamps
# persistent lockout accounts file
# reading and checking locked accounts
# SHA256 hashed passwords




import hashlib
from datetime import datetime
from getpass import getpass


LOCKED_FILE = "/home/jerram/locked_accounts.txt"
AUDIT_FILE = "/home/jerram/audit_log.txt"


users = {
        "richard": "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae",
        "alice": "1772d0119cc344f719853b2c032c2921398636766efd3ed2ffbad1c798e2bd97",
        "bob": "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae"
        }

def log_action(username, action):
    now = datetime.now()
    with open(AUDIT_FILE, "a") as f:
        f.write(f"{now} | {username} | {action}\n")
        
def is_locked(username):
    try:
        with open(LOCKED_FILE, "r") as f:
            locked = f.read().splitlines()
        return username in locked
    except FileNotFoundError:
        return False
            
def lock_account(username):
    with open(LOCKED_FILE, "a") as f:
        f.write(username + "\n")                    
            
attempts = 0

username = input("Enter username:")

if is_locked(username):
    print("this account is permanently locked. Contact your administraor.")
    log_action(username, "Attempted login on locked account")
else:
    while attempts <3:
        password = getpass("Enter password:")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username in users:
           if users[username] == hashed_password:
               print("Access granted. Welcome" + username)
               log_action(username, "Successful login")
               break
           else:
               print("Wrong password.")
               log_action(username, "Failed login attempt")
               attempts = attempts + 1
        else:
          print("username not recognised.")
          log_action(username, "unkown username attemped")
          attempts = attempts +1
            
    if attempts ==3:
        print("Account Locked. Too many failed attemps.")
        lock_account(username)
        log_action(username, "account permanently locked")
        